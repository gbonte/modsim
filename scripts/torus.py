import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters (replacing global variables)
sigma = 10
r = 28
b = 2.66

# Time span and initial condition
tf = 500
x0 = [0.5002, 0.0023, -0.0791]

# Define the system of ODEs
def f(t, x):
    dxdt = [
        x[1] + 2 * x[0] * x[1] + x[0] * x[2],
        1 - 2 * x[0]**2 + x[1] * x[2],
        x[0] - x[0]**2 - x[1]**2
    ]
    return dxdt

# Solve the system
sol = solve_ivp(f, [0, tf], x0, max_step=0.1, dense_output=True)
t = sol.t
x = sol.y.T

# 3D trajectory plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x[:, 0], x[:, 1], x[:, 2])
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('x₃')
ax.view_init(30, 30)
plt.tight_layout()
plt.show(block=False)
input("Press Enter to start the time series plots...")
# Time series plots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))  # 1 row, 3 columns

for j in range(3):
    axes[j].plot(t, x[:, j])
    axes[j].set_xlabel('Time')
    axes[j].set_ylabel(f'x_{j+1}')
    axes[j].set_title(f'Time evolution of x_{j+1}')
    axes[j].grid(True)

plt.tight_layout()



plt.show(block=False)

input("Press Enter to start the animation...")
# Animation-like progressive 3D plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0, len(x), 50):
    ax.clear()
    ax.plot(x[:i+1, 0], x[:i+1, 1], x[:i+1, 2])
    ax.set_xlim([np.min(x[:, 0]), np.max(x[:, 0])])
    ax.set_ylim([np.min(x[:, 1]), np.max(x[:, 1])])
    ax.set_zlim([np.min(x[:, 2]), np.max(x[:, 2])])
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.set_zlabel('x₃')
    ax.view_init(30, 30)
    plt.draw()
    plt.pause(0.01)
plt.ioff()
plt.show(block=False)