#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from atir import *


bound = boundary(1.5, 1, .1, set="n")
theta_i = np.arange(0, np.pi/2, .01)
theta_i_degrees = theta_i*180/np.pi
ref = reflection(theta_i, bound)

print "epsilon_i: ", bound.e2i

# Set up Q4 p_tz plot
axp_tz4 = plt.subplot(2,2,1)
axp_tz4.set_xlabel('Incidence Angle')
axp_tz4.set_ylabel('p_tz\' and p_tz\'\'')
axp_tz4.set_title('Wave Number, p_tz (Q4 solution)')
plt.plot(theta_i_degrees, ref.p_tz[4].real, 'blue')
plt.plot(theta_i_degrees, ref.p_tz[4].imag, 'r--')

# Set up Q2 p_tz plot
axp_tz2 = plt.subplot(2,2,2)
axp_tz2.set_xlabel('Incidence Angle')
axp_tz2.set_ylabel('p_tz\' and p_tz\'\'')
axp_tz2.set_title('Wave Number, p_tz (Q2 solution)')
plt.plot(theta_i_degrees, ref.p_tz[2].real, 'blue')
plt.plot(theta_i_degrees, ref.p_tz[2].imag, 'r--')


# Set up Q4 Reflectivity plot
axR4 = plt.subplot(2,2,3)
axR4.set_xlabel('Incidence Angle')
axR4.set_ylabel('Reflectivity R')
axR4.set_title('Reflectivity, R (Q4 solution)')
plt.plot(theta_i_degrees, ref.R[4])


# Set up Q2 Reflectivity plot
axR2 = plt.subplot(2,2,4)
axR2.set_xlabel('Incidence Angle')
axR2.set_ylabel('Reflectivity R')
axR2.set_title('Reflectivity, R (Q2 solution)')
plt.plot(theta_i_degrees, ref.R[2])

# Show the actual plot
plt.show()

