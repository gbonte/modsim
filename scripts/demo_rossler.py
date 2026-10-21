import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 0.2
b = 0.2
c = 5.7

# Time span and initial condition
tf = 200
x0 = [1, 0, 1]

# System of ODEs
def f(t, x):
    dxdt = [
        -x[2] - x[1],
        x[0] + a * x[1],
        x[2] * (x[0] - c) + b
    ]
    return dxdt

# Solve the system
sol = solve_ivp(f, [0, tf], x0, max_step=0.005)
t = sol.t
x = sol.y.T



# 3D animated trajectory
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0, len(x), 10):
    ax.clear()
    ax.plot(x[:i+1, 0], x[:i+1, 1], x[:i+1, 2])
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.set_zlabel('x₃')
    ax.view_init(30, 30)
    plt.draw()
    plt.pause(0.001)
plt.ioff()
plt.show()