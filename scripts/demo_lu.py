import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 1
b = 1
c = 19  # You override c = 28 with c = 19
k = -0.25

# Time span and initial condition
tf = 100
x0 = [1, 1, 1]

# System of ODEs
def f(t, x):
    dxdt = [
        36 * (x[1] - x[0]),
        c * x[1] - x[0] * x[2],
        x[0] * x[1] - 3 * x[2]
    ]
    return dxdt

# Solve the system
sol = solve_ivp(f, [0, tf], x0, max_step=0.01)
t = sol.t
x = sol.y.T



# 3D animated trajectory
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
i0=50
for i in range(i0, len(x), 10):
    ax.clear()
    ax.plot(x[i0:i+1, 0], x[i0:i+1, 1], x[i0:i+1, 2])
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.set_zlabel('x₃')
    ax.view_init(30, 30)
    plt.draw()
    plt.pause(0.01)
plt.ioff()
plt.show()