#! /usr/bin/env python
#import matplotlib; matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6, 1)
V = [0, 4, 5, 3, 4]
I = [0, 0, 0, 0, 0]

# Voltage Plot
axV = plt.subplot(1,2,1)
plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
axV.plot(t, V)

# Current Plot
axI = plt.subplot(1,2,2)
plt.xlabel('time (s)')
plt.ylabel('Current (A)')
axI.plot(t, I)

#plt.savefig("graphs.eps")
plt.show()
