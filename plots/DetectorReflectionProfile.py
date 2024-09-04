#! /usr/bin/env python

import matplotlib.pyplot as plt
from numpy.fft import fftshift
import numpy as np
from atir import *

n1 = 1.5
n2 = 1.0
gamma = 0.01
bound = boundary(n1, n2, gamma, set="n")

polarization = "p"
beam = gaussian_beam(20, polarization = polarization)
theta_i = bound.theta_c
gref = gaussian_reflection(beam, bound, theta_i, N=2**8)

# Set up the beam plot axes
ax_beam = plt.subplot(1,2,1)
plt.xlabel(r"Transverse Position, $x'$, and $x''$ (wavelengths)")
plt.ylabel(r'Beam intensity $|E|^2$, 200 wavelengths from surfacez')

# Set up coefficient axes
ax_c = plt.subplot(1,2,2)
ax_c.set_xlim(0, gref.kx.max())
plt.xlabel(r'$k_x$')
plt.ylabel('Reflection Coefficients and Incident beam on surface')

# Plot Beam
ax_beam.plot(gref.x, abs(beam.E(gref.x, 0, -2000)) ** 2, 'black', label=r'$|E_i|^2$')
ax_beam.plot(gref.x, abs(beam.E(gref.x, 0, -20)) ** 2, 'black', label=r'$|E_i|^2$')
#ax_beam.plot(gref.x, gref.E_i.real, 'blue', label='E real')
#ax_beam.plot(gref.x, gref.E_i.imag, 'r--' , label='E imag')
ax_beam.plot(gref.x, abs(gref.E_r(gref.x, 200, False)) ** 2 , 'b--', label=r'$|E_r|^2$')

# Plot transform and coefficients
ax_c.plot(fftshift(gref.kx), abs(fftshift(gref.r)) ** 2, 'black', label='R')
#ax_c.plot(fftshift(gref.kx), abs(fftshift(gref.F_i))**2, 'blue')
ax_c.plot(fftshift(gref.kx), fftshift(gref.F_i.real), 'blue', label=r'$E_i(k_x)$ (real)')
ax_c.plot(fftshift(gref.kx), fftshift(gref.F_i.imag), 'r--', label=r'$E_i(k_x)$ (imag)')



# Show the actual plot
plt.suptitle('Comparison of incident and reflected intensity profiles of Gaussian beams in ' + polarization + ' polarization\n Incident angle: ' + str(theta_i * 180/np.pi))
ax_beam.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
ax_c.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.show()

