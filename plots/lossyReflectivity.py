#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
theta_i = np.arange(0, np.pi/2, .01)
theta_i_degrees = theta_i * 180 / np.pi

#Lossless boundary
gamma = 0
bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound, polarization="p")
plt.plot(theta_i_degrees, ref.R[4], 'red', label=r'Lossless ($\gamma=0$)')

#Lossy boundary
gamma = -.5
bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound, polarization="p")
plt.plot(theta_i_degrees, ref.R[4], 'blue', label=r'Lossy ($\gamma=-\frac{1}{2}$)')


# Create the actual plot
plt.xlabel('Incidence Angle (Degrees)')
plt.ylabel('Reflectivity, R')
plt.ylim([0, 1.1])
plt.title('Attenuated Reflectivity from a Lossy Boundary')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-lossyReflectivity.eps")

