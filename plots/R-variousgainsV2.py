#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from atir2 import *

n1 = 1.5
n2 = 1
theta_i = np.arange(0, np.pi/2, .001)
theta_i_degrees = theta_i * 180 / np.pi

# Gain of 0
gamma = 0

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'red', label=r'$\gamma=0.0$')

# Gain of .01
gamma = .01

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'orange', label=r'$\gamma=0.0$')

# Gain of .03
gamma = .03

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'yellow', label=r'$\gamma=0.0$')
'''
# Gain of .1
gamma = .1

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'green', label=r'$\gamma=0.0$')

# Gain of .3
gamma = .3

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'blue', label=r'$\gamma=0.0$')

# Gain of .5
gamma = .5

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'b--', label=r'$\gamma=0.0$')

# Gain of 1
gamma = .8

bound = boundary(n1, n2, gamma, set="n")
plt.plot(theta_i_degrees, bound.R(theta_i), 'purple', label=r'$\gamma=0.0$')
'''
# Create the actual plot
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title('Reflectivities at Various Gains.')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.show()

