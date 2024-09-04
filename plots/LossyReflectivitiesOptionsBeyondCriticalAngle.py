#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
gamma = -.01
bound = boundary(n1, n2, gamma, set="n")
theta_i = np.arange(bound.theta_c, np.pi/2, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

plt.plot(theta_i_degrees, ref.R[4], 'red', label='Quadrant 1')
plt.plot(theta_i_degrees, ref.R[2], 'b--', label='Quadrant 3')


# Create the actual plot
plt.ylim(0,2.5)
plt.xlim(bound.theta_c*180/np.pi, 90)
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title(r'Plane wave reflectivity options, $R$, for incidence on a lossy medium, $\theta_i<\theta_c$')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.savefig("fig-LossyReflectivitiesOptionsBeyondCriticalAngle.eps")
#plt.show()
