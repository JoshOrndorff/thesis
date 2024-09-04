#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from atir import *

norm = True
polarization = "p"
beam = gaussian_beam(10)

N = 2 ** 10
xlim = 400.0
xp = np.linspace(-xlim, xlim, N)
k = 2 * np.pi * np.fft.fftfreq(N, 2*xlim/(N-1))

# Set up the spacial plot axes
ax = plt.subplot(1,2,1)
plt.xlabel(r"$x'$")
plt.ylabel(r'$|E|^2$')
ax.plot(xp,0*xp, "black")

# Set up the wave number plot axes
ak = plt.subplot(1,2,2)
plt.xlabel(r"$k_{x'}$")
plt.ylabel(r'$|E|^2$')
ak.plot(k,0*k, "black")

# Plot at z'=0
zp = 0

E = beam.E(xp, 0, zp)
ax.plot(xp, abs(E)**2, "blue", label="z'=0, fft")
ak.plot(np.fft.fftshift(k), abs(np.fft.fftshift(np.fft.fft(E)))**2, "blue", label="z'=0, fft")

anaRes = beam.w0 * np.sqrt(np.pi) * np.exp(- (k * beam.w0) ** 2 / 4)
n = 1.6352 if norm else 1
ak.plot(np.fft.fftshift(k), n * abs(np.fft.fftshift(anaRes))**2, "bo", label="z'=0, analytical")


#Plot at z' not 0 (first time)
zp = 600
n = 2.156 if norm else 1
E = beam.E(xp, 0, zp)
ax.plot(xp, abs(E)**2, "red", label="z'=" + str(zp) + ", fft")
ak.plot(np.fft.fftshift(k), n * abs(np.fft.fftshift(np.fft.fft(E)))**2, "red", label="z'=" + str(zp) + ", fft")


#Plot at z' not 0 (second time)
zp = 3000
n = 9.60157 if norm else 1
E = beam.E(xp, 0, zp)
ax.plot(xp, abs(E)**2, "green", label="z'=" + str(zp) + ", fft")
ak.plot(np.fft.fftshift(k), n * abs(np.fft.fftshift(np.fft.fft(E)))**2, "green", label="z'=" + str(zp) + ", fft")



# Show the actual plot
plt.suptitle('Comparison of transforms at different z\' locations')
ax.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
ak.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
plt.show()

