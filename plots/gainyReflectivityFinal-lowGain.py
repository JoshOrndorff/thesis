#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
theta_i = np.arange(0, np.pi/2, .001)
theta_i_degrees = theta_i * 180 / np.pi
Quadrant=0

# Gain of 0
gamma = 0

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'red', label=r'$\gamma=0.0$')

# Gain of .004
gamma = .004

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'green', label=r'$\gamma=' + str(gamma) + '$')

# Gain of .008
gamma = .008

bound = boundary(n1, n2, gamma, set="n")
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[Quadrant], 'blue', label=r'$\gamma=' + str(gamma) + '$')

# Create the actual plot
plt.ylim(0,2)
plt.xlim(10, 80)
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title('Reflectivities at Various Gains. Quadrant: ' + (str(Quadrant) if Quadrant != 0 else 'mixed'))
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.text(15, 1.8,
	r'$n_1$: ' + str(n1) + '\n' + r'$n_2$: ' + str(n2),
     horizontalalignment='left',
     verticalalignment='center')
plt.savefig("fig-gainyReflectivityFinal-lowGain.eps")

