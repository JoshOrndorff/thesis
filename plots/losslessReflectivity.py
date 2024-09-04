#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
gamma = 0
theta_i = np.arange(0, np.pi/2, .001)
theta_i_degrees = theta_i * 180 / np.pi
bound = boundary(n1, n2, gamma, set="n")

#P state
ref = reflection(theta_i, bound, polarization="p")
plt.plot(theta_i_degrees, ref.R[4], 'red', label='p-state')

#S state
ref = reflection(theta_i, bound, polarization="s")
plt.plot(theta_i_degrees, ref.R[4], 'blue', label='s-state')


# Create the actual plot
plt.xlabel('Incidence Angle (Degrees)')
plt.ylabel('Reflectivity, R')
plt.ylim([0, 1.1])
plt.title('Plane Wave Reflectivity from a Lossless Boundary')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-losslessReflectivity.eps")
#plt.show()
