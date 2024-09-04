#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *
from scipy.integrate import simps

n1 = 1.5
n2 = 1
polarization = "p"
phi_degrees = np.arange(20, 60, .1)
phi = phi_degrees * np.pi / 180
beam = gaussian_beam(10, polarization=polarization)

discont=219

gamma = [.01, .02, .05]
color = ["b--", "y--", "r--"]
for n in [0, 1, 2]:
	bound = boundary(n1, n2, gamma[n], set="n")
	Ii=np.empty(0)
	Ir=np.empty(0)
	
	for current_phi in phi:
		gref = gaussian_reflection(beam, bound, current_phi)
		gref.transform_fft()
		Ii = np.append(Ii, simps(abs(gref.F_i)**2, gref.x, even='first'))
		Ir = np.append(Ir, simps(abs(gref.F_r)**2, gref.x, even='first'))
	
	plt.plot(phi_degrees, Ir/Ii, color[n], label=r'$\gamma=' + str(gamma[n]) + '$')

# Create the actual plot
#plt.xlim(phi_degrees.min(), phi_degrees.max())
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title('Finite Beam Reflectivities at Various Spot Sizes')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-finiteBeamReflectivityVariousGains.eps")
#plt.show()

