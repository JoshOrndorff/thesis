#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
theta_i = np.arange(0, np.pi/2, .001)
theta_i_degrees = theta_i * 180 / np.pi
Quadrant=4

# Gain of 0
gamma = 0

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'red', label=r'$\gamma=0.0$')

# Gain of .01
gamma = .01

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'orange', label=r'$\gamma=' + str(gamma) + '$')

# Gain of .03
gamma = .03

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'yellow', label=r'$\gamma=' + str(gamma) + '$')

# Gain of .1
gamma = .1

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'green', label=r'$\gamma=' + str(gamma) + '$')

# Gain of .3
gamma = .3

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'blue', label=r'$\gamma=' + str(gamma) + '$')

# Gain of .8
gamma = .8

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'purple', label=r'$\gamma=' + str(gamma) + '$')

# Create the actual plot
plt.ylim(0, 1.1)
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title('Reflectivities at Various Gains. Quadrant: 4. Polarization: P')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig('fig-Q4ReflectivityP.eps')
