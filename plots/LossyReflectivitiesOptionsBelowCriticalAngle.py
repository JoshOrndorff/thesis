#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir import *

n1 = 1.5
n2 = 1
gamma = -.07
bound = boundary(n1, n2, gamma, set="n")
theta_i = np.arange(0, bound.theta_c, .00001)
theta_i_degrees = theta_i * 180 / np.pi
ref = reflection(theta_i, bound)

# Set up the Q1 plot axes
axq1 = plt.subplot(1,2,1)
plt.xlabel('Incident Angle')
plt.ylabel(r'Reflectivity, $R$')
plt.xlim(0,bound.theta_c*180/np.pi)

# Set up the Q3 plot axes
axq3 = plt.subplot(1,2,2)
plt.xlabel('Incident Angle')
plt.xlim(0,bound.theta_c*180/np.pi)

axq1.plot(theta_i_degrees, ref.R[4], 'red', label='Quadrant 1')
axq3.plot(theta_i_degrees, ref.R[2], 'blue', label='Quadrant 3')


# Create the actual plot
plt.xlim(0,bound.theta_c*180/np.pi)
plt.suptitle(r'Plane wave reflectivity options, $R$, for incidence on a lossy medium, $\theta_i<\theta_c$')
axq1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
axq3.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-LossyReflectivitiesOptionsBelowCriticalAngle.eps")
#plt.show()
