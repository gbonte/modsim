import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 1
b = 1
c = 28
k = -0.25

# Time span and initial condition
tf = 100
x0 = [1, 1, 1]

# System of ODEs
def f(t, x):
    dxdt = [
        35 * (x[1] - x[0]),
        (c - 35) * x[0] + c * x[1] - x[0] * x[2],
        x[0] * x[1] - 3 * x[2]
    ]
    return dxdt

# Solve the system
sol = solve_ivp(f, [0, tf], x0, max_step=0.001)
t = sol.t
x = sol.y.T

# Optional: time series plots (commented out in original)
# fig, axes = plt.subplots(1, 3, figsize=(15, 4))
# for j in range(3):
#     axes[j].plot(t, x[:, j])
#     axes[j].set_xlabel('Time')
#     axes[j].set_ylabel(f'x_{j+1}')
#     axes[j].set_title(f'Time evolution of x_{j+1}')
#     axes[j].grid(True)
# plt.tight_layout()
# plt.show()

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
    plt.pause(0.01)
plt.ioff()
plt.show()