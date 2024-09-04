#! /usr/bin/env python

import matplotlib; matplotlib.use("svg")

import matplotlib.pyplot as plt
import numpy as np
from atir import *

numsamples = 2 ** 6
xmax = -8
x = np.linspace(-xmax, xmax, numsamples)

beam = gaussian_beam(3,7)
E = beam.E(x, 0, .00001)

ax_x = plt.subplot(2,1,1)
ax_x.plot(x, E.real)
#ax_x.plot(x, E.imag)

trans = np.fft.fftshift(np.fft.fft(E))
kspace = np.fft.fftshift(np.fft.fftfreq(x.size, 2 * xmax / numsamples)) #fencepost error? I don't think so...

ax_k = plt.subplot(2,1,2)
ax_k.plot(kspace, trans.real)
#ax_k.plot(kspace, trans.imag)
plt.xlim(-.08, .08)

'''
#Transform back to be sure everything is kosher
Enew = np.fft.ifft(np.fft.ifftshift(trans))

ax_Enew = plt.subplot(3,1,3)
ax_Enew.plot(x, Enew.real)
ax_Enew.plot(x, Enew.imag)
'''

# Show the actual plot
#plt.show()
plt.savefig("FourierDaigram")

