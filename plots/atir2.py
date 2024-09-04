import numpy as np
import numpy.fft as fft
from scipy.integrate import quad

class boundary:
	def __init__(self, m1, m2real, m2gain, set="n"):
		if set=="n":
			self.n1 = m1
			self.n2 = m2real
			self.gamma = m2gain
			self.e1 = m1 ** 2
			self.e2 = complex(m2real ** 2 - m2gain ** 2,  -2 * m2real * m2gain)
		elif set=="e":
			self.e1 = m1
			self.e2 = complex(m2real, m2gain)
			#maybe calculate the other n's if necessary
			self.n1 = np.sqrt(m1)
		else:
			raise ValueError("Invalid set type. Must specify one of the following:\n n: refractive indicies\n e: permittivities")
		self.theta_c = np.arcsin(np.sqrt(self.e2.real / self.e1))
		
	def r(self, theta_i, polarization = "p"):
		p_iz = self.n1 * np.cos(theta_i)
		# Calculate p_tz
		a = self.e2.real - self.e1 * (np.sin(theta_i))**2
		b = self.e2.imag
		
		real_part = np.sqrt(np.sqrt(a**2 + b**2) + a) / np.sqrt(2)
		imag_part = np.sqrt(np.sqrt(a**2 + b**2) - a) / np.sqrt(2)
		imag_part = np.where(b < 0, -imag_part, imag_part) # Basically a sign function, but treats b=0
		
		p_tz = real_part + imag_part * 1j
		p_tz = np.where(self.e2.imag < 0 and theta_i > self.theta_c, -p_tz, p_tz)
	
		if polarization == "p":
			return (self.e1 * p_tz - self.e2 * p_iz) / (self.e1 * p_tz + self.e2 * p_iz)
		elif polarization == "s":
			return (p_tz - p_iz) / (p_tz + p_iz)
		else:
			raise ValueError("Polarization must be set to either 'p' or 's'")
		
		return (real_num / denom) + (imag_num / denom) * 1j
		
	def R(self, theta_i, polarization="p"):
		return abs(self.r(theta_i, polarization)) ** 2



class gaussian_beam:
	def __init__(self, w0, E0 = 1, wavelength = 1, polarization="p"):
		# Distance units for all parameters are in wavelengths
		self.E0 = E0
		self.w0 = w0
		self.wavelength = wavelength
		self.polarization = polarization
		self.rayleighRange = np.pi * w0 ** 2 / wavelength
		self.k = 2 * np.pi / wavelength
		self.divergence = wavelength / (np.pi * w0)
		
	def w(self, z, approx = False):
		return self.w0 * np.sqrt(1 + (z / self.rayleighRange) ** 2) 
		
	def curvatureRadius(self, z):
		z = np.where(z != 0, z, float("inf")) # To avoid division by zero when z=0
		return z + self.rayleighRange ** 2 / z
	
	def gouy(self, z):
		return np.arctan(z / self.rayleighRange)
		
	def complexParameter(self, z):
		return z + self.rayleighRange * 1j  # z + iz_R
		
	def E(self, x, y, z, approx = False):
		rsq = x ** 2 + y ** 2
		if approx:
			exponent = -rsq/(self.w0 ** 2) + 1j * self.k * z + 1j * z / self.rayleighRange
			coefficient = self.E0
		else:
			exponent = -rsq/(self.w(z) ** 2) + 1j * self.k * (z - rsq/(2 * self.curvatureRadius(z))) + 1j * self.gouy(z)
			coefficient = self.E0 * self.w0/self.w(z)
		
		return  coefficient * np.exp(exponent)
		
class gaussian_reflection:
	def __init__(self, i_beam, boundary, phi = None):
		self.i_beam = i_beam
		self.boundary = boundary
		self.phi = phi if phi is not None else boundary.theta_c
		
	def transform_analytical(self, theta_i):
		coefficient = self.i_beam.E0 * self.i_beam.w0 * np.sqrt(np.pi) / np.cos(self.phi)
		exponent = -self.i_beam.k ** 2 * self.i_beam.w0 ** 2 * (np.sin(self.phi) - np.sin(theta_i)) ** 2 / (4 * np.cos(self.phi) ** 2)
		return  coefficient * np.exp(exponent)
		
	def E_r_analytical(self, x, z):
		if np.atleast_1d(x).size != np.atleast_1d(z).size:
			if np.atleast_1d(x).size == 1:
				x = x * np.ones(z.size)
			elif np.atleast_1d(z).size == 1:
				z = z * np.ones(x.size)
			else:
				raise ValueError('x and z must have same first dimension')
				
		E = np.empty(0) #should be len(x) maybe
		for n in range(0, np.atleast_1d(x).size):
			real_part = quad(lambda theta: \
			(self.transform_analytical(theta) * self.boundary.r(theta, self.i_beam.polarization) \
			* np.exp(1j*self.i_beam.k*(x[n]*np.sin(theta)+z[n]*np.cos(theta)))).real \
			,0, np.pi/2)
			
			imag_part = quad(lambda theta: \
			(self.transform_analytical(theta) * self.boundary.r(theta, self.i_beam.polarization) \
			* np.exp(1j*self.i_beam.k*(x[n]*np.sin(theta)+z[n]*np.cos(theta)))).imag \
			,0, np.pi/2)
			
			E = np.append(E, complex(real_part[0], imag_part[0]))
		return E
	
	def transform_fft(self, N = 2 ** 8):
		self.N = N
		self.xmax = N * self.i_beam.wavelength/4
		self.x = np.linspace(-self.xmax, self.xmax, N)
		
		# Transform the i_beam and store member variables
		xpb = self.x * np.cos(self.phi)
		zpb = self.x * np.sin(self.phi)
		self.E_i = self.i_beam.E(xpb, 0, zpb)
		self.F_i = fft.fft(self.E_i)
		self.kx = 2 * np.pi * fft.fftfreq(N, .5)
		self.kz = np.sqrt(self.i_beam.k ** 2 - self.kx ** 2)
		self.theta_i = np.arcsin((self.kx * self.i_beam.wavelength) / (2 * np.pi))
		
		# Multiply by reflection coefficients
		self.r = self.boundary.r(self.theta_i, self.i_beam.polarization)
		self.F_r = self.r * self.F_i
		
		# Surface inverse transform
		self.E_r_surface = fft.ifft(self.F_r)
		
	def E_r_fft(self, x, z, unprimed_coordinates = True):		
		self.kxpp = -self.kx * np.cos(self.phi) - self.kz * np.sin(self.phi)
		self.kzpp =  self.kx * np.sin(self.phi) - self.kz * np.cos(self.phi)
		
		if np.atleast_1d(x).size != np.atleast_1d(z).size and np.atleast_1d(x).size != 1 and np.atleast_1d(z).size != 1:
			raise ValueError('x and z must have same first dimension')
		
		(kx, kz) = (self.kx, self.kz) if unprimed_coordinates else (self.kxpp, self.kzpp)
				
		E = np.empty(0) #should be len(x) maybe
		for thisx in np.nditer(x):
			exponent = 1j * (kx * thisx + kz * z)
			E = np.append(E, np.sum(self.F_r * np.exp(exponent)))
			
		return np.fft.fftshift(E)/np.sqrt(self.N*x.size)
