#! /usr/bin/env python

#import matplotlib
#matplotlib.use('SVG')

import matplotlib.pyplot as plt
import numpy as np
from atir import *

e1 = 2.338
e2r = 2.277

#Set up the Mansuripur plot axes
axr = plt.subplot(1,2,1)
#plt.ylim(0.95, 1.3)
plt.xlim(80.7, 81)
plt.xlabel('Incidence Angle')
plt.ylabel(r'$|E_r / E_i| = \sqrt{R}$')

# set up the actual reflectivity plot axes
axR = plt.subplot(1,2,2)
#plt.ylim(0.9, 1.7)
plt.xlim(80.7, 81)
plt.xlabel('Incidence Angle')
plt.ylabel(r'$R$')

# Black Line
e2i = 0

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

axr.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'black', label=r"$\epsilon_2' =" + str(e2i) + "$")
axR.plot(theta_i_degrees, ref.R[2], 'black', label=r"$\epsilon_2' =" + str(e2i) + "$")

# Green Line
e2i = -.08

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

axr.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'green', label=r"$\epsilon_2' =" + str(e2i) + "$")
axR.plot(theta_i_degrees, ref.R[2], 'green', label=r"$\epsilon_2' =" + str(e2i) + "$")

# Cyan Line
e2i = -.05

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

axr.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'cyan', label=r"$\epsilon_2' =" + str(e2i) + "$")
axR.plot(theta_i_degrees, ref.R[2], 'cyan', label=r"$\epsilon_2' =" + str(e2i) + "$")

# Green Line
e2i = -.06

bound = boundary(e1, e2r, e2i, set="e")
theta_i = np.arange(bound.theta_c, 1.42, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

axr.plot(theta_i_degrees, np.sqrt(ref.R[2]), 'purple', label=r"$\epsilon_2' =" + str(e2i) + "$")
axR.plot(theta_i_degrees, ref.R[2], 'purple', label=r"$\epsilon_2' =" + str(e2i) + "$")

# Show the actual plot
plt.suptitle('Single surface reflectivity using the parameters from Koester\'s fiber experiment')
axr.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
axR.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.show()
#plt.savefig('myfig')
