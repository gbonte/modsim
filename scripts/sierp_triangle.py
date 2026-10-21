
import numpy as np
import matplotlib.pyplot as plt

# Chapter 5 - Fractals and Multifractals.
# Program_5b - The Sierpinski triangle.
# Copyright Birkhauser 2004. Stephen Lynch.

# The Sierpinski triangle (Figure 5.6).
# The vertices of the triangle.
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([2, 2*np.sqrt(3)])

# The number of points to be plotted.
Nmax = 500000
P = np.zeros((Nmax+1, 2))
scale = 1/2

for n in range(Nmax):
    r = np.random.rand()
    if r < 1/3:
        P[n+1, :] = P[n, :] + (A - P[n, :]) * scale
    elif r < 2/3:
        P[n+1, :] = P[n, :] + (B - P[n, :]) * scale
    else:
        P[n+1, :] = P[n, :] + (C - P[n, :]) * scale

plt.plot(P[:, 0], P[:, 1], '.', markersize=1)

plt.axis([0, 4, 0, 2*np.sqrt(3)])
ax = plt.gca()
ax.set_position([0, 0, 1, 1])
plt.title('The Sierpinski triangle')
plt.show()

# End of Program_5b.

