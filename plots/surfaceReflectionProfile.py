#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
from numpy.fft import fftshift
import numpy as np
from atir2 import *

n1 = 1.5
n2 = 1.0
gamma = 0.01
bound = boundary(n1, n2, gamma, set="n")

polarization = "p"
beam = gaussian_beam(50, polarization = polarization)
phi = bound.theta_c
gref = gaussian_reflection(beam, bound, phi)
gref.transform_fft(N=2**10)

gref.theta_i_degrees = gref.theta_i * 180 / np.pi
theta_i = np.arange(0, np.pi, .0001)
theta_i_degrees = theta_i * 180/np.pi

plt.figure(1, figsize=(14,8))
plt.subplots_adjust(left=.1, wspace=.35)

# Incident plot #########################
ax_incident = plt.subplot(1,3,1)
plt.xlabel(r'Position Along Surface ($\lambda$)')
plt.ylabel(r'Incident Beam Intensity ($E_0^2$)')
plt.xlim(-250, 250)

ax_incident.plot(gref.x, abs(gref.E_i) ** 2, 'black', label=r'$|E_i|^2$')
	#ax_incident.plot(gref.x, gref.E_i.real, 'blue', label='E real')
	#ax_incident.plot(gref.x, gref.E_i.imag, 'r--' , label='E imag')

# Coefficients and Transform plot ##############
ax_c = plt.subplot(1,3,2)
ax_c.set_xlim(0, 90)
plt.xlabel(r'$\theta_i$ (degrees)')
plt.ylabel('Reflection Coefficients and Incident Beam Transform (A.U.)')
plt.xlim(40,45)
plt.ylim(0,4)

ax_c.plot(theta_i_degrees, bound.R(theta_i), 'black', label=r'$R(\theta_i)$')

ax_c.plot(fftshift(gref.theta_i_degrees), abs(fftshift(gref.F_i))**2/gref.N/20, 'b--', label=r'$|E_i(\theta_i)|^2$, FFT')
	#ax_c.plot(fftshift(gref.theta_i_degrees), fftshift(gref.F_i.real), 'blue', label=r'$E_i(\theta_i)$ (real)')
	#ax_c.plot(fftshift(gref.theta_i_degrees), fftshift(gref.F_i.imag), 'r--', label=r'$E_i(\theta_i)$ (imag)')

ax_c.plot(theta_i_degrees, gref.transform_analytical(theta_i)/np.pi/13, color="magenta", ls="dotted", label=r'$|E_i(\theta_i)|^2$, analytical')

# Reflected Plot ###################################
ax_reflected = plt.subplot(1,3,3)
plt.xlabel(r'Position Along Surface ($\lambda$)')
plt.ylabel('Reflected Beam Intensity (A.U.)')
plt.xlim(-250, 250)

ax_reflected.plot(gref.x, abs(gref.E_r_surface) ** 2, 'b--', label=r'$|E_r|^2$, FFT')

newx = np.arange(-250, 250, 5)
era = gref.E_r_analytical(newx,0)
ax_reflected.plot(newx, abs(era) ** 2 / 1.6, color='magenta', ls="dotted", label=r'$|E_r|^2$, analytical')


# Show the actual plot
plt.suptitle('Comparison of incident and reflected intensity profiles of Gaussian beams in ' + polarization + ' polarization\n' + r'Incidence at critical angle, $\phi = \theta_c$')
ax_incident.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
ax_c.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
ax_reflected.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.savefig("fig-surfaceReflectionProfile.eps")
plt.show()

