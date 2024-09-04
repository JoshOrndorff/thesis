#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *
from scipy.integrate import simps

n1 = 1.5
n2 = 1
gamma = .01
bound = boundary(n1, n2, gamma, set="n")
polarization = "s"
phi_degrees = np.arange(20, 60, .1)
phi = phi_degrees * np.pi / 180

discont=219
plt.plot(phi_degrees[:discont], bound.R(phi, polarization=polarization)[:discont], 'black', label=r'$w_0\to\infty$'+'\n'+'(Plane Wave)')
plt.plot(phi_degrees[discont:], bound.R(phi, polarization=polarization)[discont:], 'black')

w0 = [12, 5, 2]
color = ["b--", "y--", "r--"]
for n in [0, 1, 2]:
	Ii=np.empty(0)
	Ir=np.empty(0)
	beam = gaussian_beam(w0[n], polarization=polarization)
	
	for current_phi in phi:
		gref = gaussian_reflection(beam, bound, current_phi)
		gref.transform_fft()
		Ii = np.append(Ii, simps(abs(gref.F_i)**2, gref.x, even='first'))
		Ir = np.append(Ir, simps(abs(gref.F_r)**2, gref.x, even='first'))
	
	plt.plot(phi_degrees, Ir/Ii, color[n], label=r'$w_0=' + str(w0[n]) + '$')

# Create the actual plot
plt.xlim(phi_degrees.min(), phi_degrees.max())
plt.xlabel('Incidence Angle')
plt.ylabel('Reflectivity, R')
plt.title('Finite Beam Reflectivities at Various Spot Sizes')
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
plt.savefig("fig-finiteBeamReflectivityS.eps")
#plt.show()

