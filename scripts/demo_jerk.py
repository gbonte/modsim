import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 1
b = 1
c = -2.5  # You override -2.625 with -2.5
k = -0.25

# Initial condition and time span
tf = 500
x0 = [0, 0, 1]

# System of ODEs
def f(t, x):
    dxdt = [
        x[1],
        x[2],
        -a * x[2] - b * x[1] - c * x[0] + k * x[0] * abs(x[0])
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
for i in range(0, len(x), 10):
    ax.clear()
    ax.plot(x[:i+1, 0], x[:i+1, 1], x[:i+1, 2])
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.set_zlabel('x₃')
    ax.view_init(30, 30)
    plt.draw()
    plt.pause(0.001)

print("Done")
plt.ioff()
plt.show()