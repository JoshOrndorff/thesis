#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *

polarization = "p"
w0 = 5
beam = gaussian_beam(w0, polarization=polarization)
bound = boundary(1.5, 1, 0, set="n")
theta_i = np.arange(-np.pi/2, np.pi/2, .01)
theta_i_degrees = theta_i * 180 / np.pi

#First Angle
phi = bound.theta_c-.2
gref = gaussian_reflection(beam, bound, phi)
gref.transform_fft(N=2**9)

plt.plot(theta_i_degrees, gref.transform_analytical(theta_i), "blue", label="Real Part, Analytical")
plt.plot(theta_i_degrees, 0*theta_i_degrees, "red", label="Imag Part, Analytical")
plt.plot(gref.theta_i*180/np.pi, gref.F_i.real, "b--", label="Real Part, FFT")
plt.plot(gref.theta_i*180/np.pi, gref.F_i.imag, "r--", label="Real Part, FFT")

plt.text(31, -20,
	r'$\phi = ' + str(round(phi*180/np.pi)) + '^o$' + '\n' + r'$N = 2^9$',
     horizontalalignment='center',
     verticalalignment='center')

#Second Angle
phi = bound.theta_c+.2
gref = gaussian_reflection(beam, bound, phi)
gref.transform_fft(N=2**8)

plt.plot(theta_i_degrees, gref.transform_analytical(theta_i), "blue")
plt.plot(theta_i_degrees, 0*theta_i_degrees, "red")
plt.plot(gref.theta_i*180/np.pi, gref.F_i.real, "b--")
plt.plot(gref.theta_i*180/np.pi, gref.F_i.imag, "r--")

plt.text(60, -20,
	r'$\phi = ' + str(round(phi*180/np.pi)) + '^o$' + '\n' + r'$N = 2^8$',
     horizontalalignment='center',
     verticalalignment='center')

# Show the actual plot
plt.xlabel(r"$\theta_i$ (degrees)")
plt.xlim(20, 70)
plt.ylim(-30, 35)
plt.ylabel(r'$|E|^2$ ($E_0$)')
plt.title('Gaussian Beam Angular Intensity Profiles \n' + r'Beam focus: $w_0=' + str(w0) + '\lambda$')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-transformComparisonVariousPhi.eps")
#plt.show()

