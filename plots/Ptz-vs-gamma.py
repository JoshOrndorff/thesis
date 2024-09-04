#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from atir import *

n1 = 1.5
n2 = 1.0
gamma = np.arange(-.3, .3, .001)
bound = boundary(n1, n2, gamma, set="n")

theta_c_mean = np.mean(bound.theta_c)		# Mean critical angle (actual critical angle depends on gamma and varies by about a degree)
theta_l = theta_c_mean - .5 				# Half a radian (~28degrees) below the critical angle
theta_h = theta_c_mean + .5				# Half a radian (~28degrees) beyond the critical angle



# Set up axes for theta_l graphs
ref = reflection(theta_l, bound)

axQ2l = plt.subplot(2,3,1)
axQ2l.set_xlabel(r'gain, $\gamma$')
axQ2l.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ2l.set_title(r'Quadrant 2 or 3, $\theta < \theta_c$')
plt.plot(gamma, ref.p_tz[2].real, 'blue')
plt.plot(gamma, ref.p_tz[2].imag, 'r--')

axQ4l = plt.subplot(2,3,4)
axQ4l.set_xlabel(r'gain, $\gamma$')
axQ4l.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ4l.set_title(r'Quadrant 1 or 4, $\theta < \theta_c$')
plt.plot(gamma, ref.p_tz[4].real, 'blue')
plt.plot(gamma, ref.p_tz[4].imag, 'r--')

# Set up axes for theta_c graphs
ref = reflection(bound.theta_c, bound)

axQ2c = plt.subplot(2,3,2)
axQ2c.set_xlabel(r'gain, $\gamma$')
axQ2c.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ2c.set_title(r'Quadrant 2 or 3, $\theta = \theta_c$')
plt.plot(gamma, ref.p_tz[2].real, 'blue')
plt.plot(gamma, ref.p_tz[2].imag, 'r--')

axQ4c = plt.subplot(2,3,5)
axQ4c.set_xlabel(r'gain, $\gamma$')
axQ4c.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ4c.set_title(r'Quadrant 1 or 4, $\theta = \theta_c$')
plt.plot(gamma, ref.p_tz[4].real, 'blue')
plt.plot(gamma, ref.p_tz[4].imag, 'r--')

# Set up axes for theta_h graphs
ref = reflection(theta_h, bound)

axQ2h = plt.subplot(2,3,3)
axQ2h.set_xlabel(r'gain, $\gamma$')
axQ2h.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ2h.set_title(r'Quadrant 2 or 3, $\theta > \theta_c$')
plt.plot(gamma, ref.p_tz[2].real, 'blue')
plt.plot(gamma, ref.p_tz[2].imag, 'r--')

axQ4h = plt.subplot(2,3,6)
axQ4h.set_xlabel(r'gain, $\gamma$')
axQ4h.set_ylabel(r"$p_{tz}'$ and $p_{tz}''$")
axQ4h.set_title(r'Quadrant 1 or 4, $\theta > \theta_c$')
plt.plot(gamma, ref.p_tz[4].real, 'blue')
plt.plot(gamma, ref.p_tz[4].imag, 'r--')

print "theta_l: ", theta_l*180/np.pi
print "theta_c: ", theta_c_mean*180/np.pi
print "theta_h: ", theta_h*180/np.pi

plt.subplots_adjust(left=.05, right=.97, bottom=.1, top=.95, wspace=.3, hspace=.3)
plt.show()






