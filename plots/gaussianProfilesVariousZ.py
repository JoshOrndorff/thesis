#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *

polarization = "p"
beam = gaussian_beam(10)

N = 2 ** 10
xlim = 50.0
xp = np.linspace(-xlim, xlim, N)


zp = 0
E = beam.E(xp, 0, zp)
plt.plot(xp, abs(E)**2, "blue", label=r"$z'=" + str(zp) + "\lambda$")

zp = 300
E = beam.E(xp, 0, zp)
plt.plot(xp, abs(E)**2, color="red", ls='dotted', label=r"$z'=" + str(zp) + "\lambda$")

zp = 1000
E = beam.E(xp, 0, zp)
plt.plot(xp, abs(E)**2, "green", ls='dashed', label=r"$z'=" + str(zp) + "\lambda$")


# Show the actual plot
plt.xlabel(r"$x'$ ($\lambda$)")
plt.xlim(-xlim, xlim)
plt.ylabel(r'$|E|^2$ ($E_0$)')
plt.title('Gaussian Beam Cross-Sectional Intensity Profiles \n' + r' Beam focus: $w_0=10\lambda$')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.savefig("fig-gaussianProfilesVariousZ.eps")
plt.show()

