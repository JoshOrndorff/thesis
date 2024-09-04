#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from atir import *

e1 = 2.338
e2r = 2.277
polarization = "s"

#Set up the Mansuripur plot axes
axR = plt.subplot(1,2,1)
plt.ylim(0.95, 1.3)
plt.xlim(80.7, 81)
plt.xlabel('Incidence Angle')
plt.ylabel(r'$\sqrt{R}$')

# set up the actual reflectivity plot axes
axr = plt.subplot(1,2,2)
plt.ylim(0.95, 1.3)
plt.xlim(80.7, 81)
plt.xlabel('Incidence Angle')
plt.ylabel(r'$|r|$')

# Black Line
e2i = 0

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound, polarization)

axR.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'black', label=r"$\epsilon_2' = 0$")
axr.plot(theta_i_degrees, abs(ref.r[2]), 'black', label=r"$\epsilon_2' = 0$")

# Green Line
e2i = -.0001

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound, polarization)

axR.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'green', label=r"$\epsilon_2' = -.0001$")
axr.plot(theta_i_degrees, abs(ref.r[2]), 'green', label=r"$\epsilon_2' = -.0001$")

# Cyan Line
e2i = -.001

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound, polarization)

axR.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'cyan', label=r"$\epsilon_2' = -.001$")
axr.plot(theta_i_degrees, abs(ref.r[2]), 'cyan', label=r"$\epsilon_2' = -.001$")

# Purple Line
e2i = -.002

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound, polarization)

axR.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'purple', label=r"$\epsilon_2' = -.002$")
axr.plot(theta_i_degrees, abs(ref.r[2]), 'purple', label=r"$\epsilon_2' = -.002$")

# Show the actual plot
plt.suptitle('Confirming agreement between calculation of r and R for ' + polarization + ' polarization')
axr.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
axR.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.show()

