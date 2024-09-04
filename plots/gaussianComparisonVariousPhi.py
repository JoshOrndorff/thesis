#! /usr/bin/env python
import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from atir2 import *

plt.figure(1, figsize=(14,10))
plt.subplots_adjust(left=.1, wspace=.35, hspace=.5)

polarization = "p"

# Top left axes
w0 = 2
beam = gaussian_beam(w0, polarization=polarization)

N = 2 ** 10
xlim = 400
x = np.linspace(-xlim, xlim, N)

axtl = plt.subplot(2,2,1)
plt.xlabel(r"$x$ ($\lambda$)")
plt.xlim(-xlim, xlim)
plt.ylabel(r'$|E|^2$ ($E_0^2$)')
plt.title('Intensity Profiles \n' + r'Beam focus: $w_0=' + str(w0) + '\lambda$')

phi = 25
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "yellow", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "y--")
'''
phi = 40
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "green", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "g--")
'''
phi = 65
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "magenta", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "m--")

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)

# Top right Axes
axtr = plt.subplot(2,2,2)
plt.xlabel(r"$x$ ($\lambda$)")
plt.xlim(-xlim, xlim)
plt.ylabel(r'$\Re(E)$ ($E_0$)')
plt.title('E-field Profiles \n' + r'Beam focus: $w_0=' + str(w0) + '\lambda$')

phi = 25
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "yellow", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "y--")
'''
phi = 40
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "green", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "g--")
'''
phi = 65
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "magenta", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "m--")

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)



# Bottom left axes
w0 = 1
beam = gaussian_beam(w0, polarization=polarization)

N = 2 ** 10
xlim = 250
x = np.linspace(-xlim, xlim, N)

axtl = plt.subplot(2,2,3)
plt.xlabel(r"$x$ ($\lambda$)")
plt.xlim(-xlim, xlim)
plt.ylabel(r'$|E|^2$ ($E_0^2$)')
plt.title('\n' + r'Beam focus: $w_0=' + str(w0) + '\lambda$')

phi = 25
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "yellow", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "y--")
'''
phi = 40
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "green", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "g--")
'''
phi = 65
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, abs(E)**2, "magenta", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, abs(E)**2, "m--")

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)

# Bottom right Axes
axtr = plt.subplot(2,2,4)
plt.xlabel(r"$x$ ($\lambda$)")
plt.xlim(-xlim, xlim)
plt.ylabel(r'$\Re(E)$ ($E_0$)')
plt.title('\n' + r'Beam focus: $w_0=' + str(w0) + '\lambda$')

phi = 25
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "yellow", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "y--")
'''
phi = 40
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "green", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "g--")
'''
phi = 65
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, False)
plt.plot(x, E.real, "magenta", label=r"$\phi=" + str(phi) + r"^o$")
E = beam.E(x*np.cos(phi)*np.pi/180, 0, x*np.sin(phi)*np.pi/180, True)
plt.plot(x, E.real, "m--")

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)



# Show the actual plot
plt.savefig("fig-gaussianComparisonVariousPhi.eps")
plt.show()

