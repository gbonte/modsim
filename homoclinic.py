import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system
def system(t, x):
    dx1 = x[1]
    dx2 = x[0] - x[0]**3
    return [dx1, dx2]

# Initial conditions
initial_conditions = [[0.0001, 0]]  # List of initial condition sets
tspan = [0, 17]

# Solve and plot
plt.figure()
for ic in initial_conditions:
    sol = solve_ivp(system, tspan, ic, rtol=1e-8, atol=1e-10)
    x = sol.y.T
    plt.plot(x[:, 0], x[:, 1])

# Label axes and show plot
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Trajectoire homoclinique du système dynamique')
plt.grid(True)
plt.tight_layout()
plt.show()