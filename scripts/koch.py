
# Chapter 5 - Fractals and Multifractals.
# Program_5a - The Koch curve.
# Copyright Birkhauser 2004. Stephen Lynch.

# Plot the Koch curve up to stage k (Figure 5.2)

import numpy as np
import matplotlib.pyplot as plt

# Clear equivalent (not needed in Python, but preserving comment structure)
# echo off (not applicable in Python)
# close all
plt.close('all')

k = 10
mmax = 4**k
x = np.zeros(mmax + 1)
y = np.zeros(mmax + 1)
h = 3**(-k)
x[0] = 0
y[0] = 0
angle = np.array([0, np.pi/3, -np.pi/3, 0])

for a in range(1, mmax + 1):
    m = a - 1
    ang = 0
    segment = np.zeros(k, dtype=int)
    for b in range(k):
        segment[b] = m % 4
        m = m // 4
        r = segment[b]
        ang = ang + angle[r]
    x[a] = x[a - 1] + h * np.cos(ang)
    y[a] = y[a - 1] + h * np.sin(ang)

plt.plot(x, y, 'b')
plt.axis('equal')
plt.show()

# End of Program_5a.

