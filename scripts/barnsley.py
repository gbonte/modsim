
import numpy as np
import matplotlib.pyplot as plt

# Chapter 5 - Fractals and Multifractals.
# Program_5c - An iterated function system.
# Copyright Birkhauser 2004. Stephen Lynch.

# Barnsley's fern (Figure 5.7).
def Program_5c(N):
    """
    This function plots Barnsley's fern with N points.
    The transformations are in the form
    T(x,y) = (a*x+b*y+c, d*x+e*y+f).
    """
    N = 500000
    P = np.zeros((N, 2))
    P[0, :] = [0.5, 0.5]
    
    # The main loop where the iterations are performed.
    for k in range(N - 1):
        r = np.random.rand()
        if r < 0.05:
            P[k + 1, :] = T(P[k, :], 0, 0, 0, 0, 0.2, 0)
        elif r < 0.86:
            P[k + 1, :] = T(P[k, :], 0.85, 0.05, 0, -0.04, 0.85, 1.6)
        elif r < 0.93:
            P[k + 1, :] = T(P[k, :], 0.2, -0.26, 0, 0.23, 0.22, 1.6)
        else:
            P[k + 1, :] = T(P[k, :], -0.15, 0.28, 0, 0.26, 0.24, 0.44)
    
    plt.figure()
    plt.plot(P[:, 0], P[:, 1], '.', markersize=1)
    plt.axis([-2.5, 3.5, 0, 11])
    ax = plt.gca()
    ax.set_position([0, 0, 1, 1])
    plt.show()


# The transformation T
def T(P, a, b, c, d, e, f):
    F = np.zeros(2)
    F[0] = a * P[0] + b * P[1] + c
    F[1] = d * P[0] + e * P[1] + f
    return F

Program_5c(100000)

# End of Program_5c.

