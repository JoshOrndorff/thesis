#! /usr/bin/env python
#import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
from numpy.fft import fftshift
import numpy as np
from atir2 import *

n1 = 1.5
n2 = 1.0
gamma = 0.0
bound = boundary(n1, n2, gamma, set="n")

polarization = "p"
beam = gaussian_beam(4, polarization = polarization)
phi = bound.theta_c
gref = gaussian_reflection(beam, bound, phi)

theta_i = np.arange(0, np.pi/2, .003)
theta_i_degrees = theta_i * 180 / np.pi
domain = .01
theta_r = np.arange(bound.theta_c - domain, bound.theta_c + domain, .0005)
theta_r_degrees = theta_r * 180 / np.pi

d = 10000 # this can cause a warning from the integrator. d=1000 caused it, d=100 didn't



plt.figure(1, figsize=(14,8))
plt.subplots_adjust(left=.1, wspace=.35)

# Coefficients and Transform plot ##############
ax_surface = plt.subplot(1,2,1)
plt.xlabel(r'$\theta_i$ (degrees)')
plt.ylabel('Reflection Coefficients and Transforms (A.U.)')

plt.plot(theta_i_degrees, bound.R(theta_i, polarization=polarization)*30+50, 'black', label=r'$R(\theta_i)$')

plt.plot(theta_i_degrees, abs(gref.transform_analytical(theta_i))**2, "blue", label=r'$|E_i(\theta_i)|^2$')
plt.plot(theta_i_degrees, abs(gref.transform_analytical(theta_i) * bound.r(theta_i, polarization=polarization))**2, "red",  label=r'$|E_r(\theta_i)|^2$')


# Detector Plot ###################################
ax_detector = plt.subplot(1,2,2)
plt.xlabel('Position Along Detector')
plt.ylabel('Reflected Beam Intensity (A.U.)')

plt.plot(theta_r_degrees, abs(gref.E_r_analytical(d*np.sin(theta_r), d*np.cos(theta_r)))**2)




# Show the actual plot
plt.suptitle('Detector Intensity')
ax_surface.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
#plt.savefig("fig-surfaceReflectionProfile.eps")
plt.show()

