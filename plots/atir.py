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
			self.e2r = m2real ** 2 - m2gain ** 2
			self.e2i = -2 * m2real * m2gain
		elif set=="e":
			self.e1 = m1
			self.e2r = m2real
			self.e2i = m2gain
			#maybe calculate the other n's if necessary
			self.n1 = np.sqrt(m1)
		else:
			raise ValueError("Invalid set type. Must specify one of the following:\n n: refractive indicies\n e: permittivities")
		self.theta_c = np.arcsin(np.sqrt(self.e2r / self.e1))
		self.tehta_c_degrees = self.theta_c * 180 / np.pi



class reflection:
	def __init__(self, theta_i, boundary, polarization="p"):
		self.theta_i = theta_i
		self.boundary = boundary
		
		#Calculating p's
		self.p_iz = boundary.n1 * np.cos(theta_i)
		self.p_tz = calc_p_tzs(boundary, theta_i)		
		#Calculating r's
		self.r = [0,0,0,0,0]
		self.r[2] = calc_r(boundary, self.p_iz, self.p_tz[2], polarization)
		self.r[4] = calc_r(boundary, self.p_iz, self.p_tz[4], polarization)
		self.r[0] = np.where(abs(theta_i) < boundary.theta_c, self.r[4], self.r[2])
		#Calculating Rs		
		self.R = [0,0,0,0,0]
		self.R[2] = calc_R(boundary, self.p_iz, self.p_tz[2], polarization)
		self.R[4] = calc_R(boundary, self.p_iz, self.p_tz[4], polarization)		
		self.R[0] = np.where(abs(theta_i) < boundary.theta_c, self.R[4], self.R[2])

def calc_p_tzs(boundary, theta_i):
	p_tz = [0,0,0,0,0]		
	a = boundary.e2r - boundary.e1 * (np.sin(theta_i))**2
	b = boundary.e2i
	
	real_part = np.sqrt(np.sqrt(a**2 + b**2) + a) / np.sqrt(2)
	imag_part = np.sqrt(np.sqrt(a**2 + b**2) - a) / np.sqrt(2)
	imag_part = np.where(b < 0, -imag_part, imag_part) # Basically a sign function, but treats b=0
		
	p_tz[4] =  real_part + imag_part*1j
	p_tz[2] = -real_part - imag_part*1j
	
	return p_tz
	
def calc_r(boundary, p_iz, p_tz, polarization="p"):
	if polarization == "p":
		real_num = boundary.e1 ** 2 * (p_tz.real ** 2 + p_tz.imag ** 2) - p_iz ** 2 * (boundary.e2r ** 2 + boundary.e2i ** 2)
		imag_num = 2 * boundary.e1 * p_iz * (p_tz.imag * boundary.e2r - p_tz.real * boundary.e2i)
		denom = (boundary.e1 * p_tz.real + boundary.e2r * p_iz) ** 2 + (boundary.e1 * p_tz.imag + boundary.e2i * p_iz) ** 2
	elif polarization == "s":
		real_num = p_iz ** 2 - p_tz.real ** 2 - p_tz.imag ** 2
		imag_num = 2 * p_iz * p_tz.imag
		denom = (p_iz + p_tz.real) ** 2 + p_tz.imag ** 2
	else:
		raise ValueError("Polarization must be set to either 'p' or 's'")
		
	return (real_num / denom) + (imag_num / denom) * 1j
	
def calc_R(boundary, p_iz, p_tz, polarization="p"):
	if polarization == "p":
		return ((boundary.e2r * p_iz - boundary.e1 * p_tz.real)**2 + (boundary.e2i * p_iz - boundary.e1 * p_tz.imag)**2) / \
		       ((boundary.e2r * p_iz + boundary.e1 * p_tz.real)**2 + (boundary.e2i * p_iz + boundary.e1 * p_tz.imag)**2)
	elif polarization == "s":
		return ((p_iz - p_tz.real) ** 2 + p_tz.imag ** 2)  /  ((p_iz + p_tz.real) ** 2 + p_tz.imag ** 2)
	else:
		raise ValueError("Polarization must be set to either 'p' or 's'")
