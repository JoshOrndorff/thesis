#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *
from scipy.integrate import simps

n1 = 1.5
n2 = 1
polarization = "p"
gamma = np.arange(0, 1, .01)
beam = gaussian_beam(10, polarization=polarization)

discont=219
phi_degrees=[]
phi = [np.pi/3, np.pi/4, np.pi/6]
for p in phi:
	phi_degrees.append(p*180/np.pi)
	
color = ["b--", "y--", "r--"]
for n in [0, 1, 2]:
	Ii=np.empty(0)
	Ir=np.empty(0)
	
	for current_gamma in gamma:
		bound = boundary(n1, n2, current_gamma, set="n")
		gref = gaussian_reflection(beam, bound, phi[n])
		gref.transform_fft(2**10)
		Ii = np.append(Ii, simps(abs(gref.F_i)**2, gref.x, even='first'))
		Ir = np.append(Ir, simps(abs(gref.F_r)**2, gref.x, even='first'))
	
	plt.plot(gamma, Ir/Ii, color[n], label=r'$\phi=' + str(phi_degrees[n]) + '$')

# Create the actual plot
#plt.xlim(phi_degrees.min(), phi_degrees.max())
plt.xlabel('Gain, $\gamma$')
plt.ylabel('Reflectivity, R')
plt.title('Finite Beam Reflectivities at Various Spot Sizes')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-finiteBeamVsGain.eps")
plt.show()

