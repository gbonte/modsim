import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Clear all variables (Python equivalent - not strictly necessary)
# In Python, we start with a clean namespace in a new script

# Close all figures
plt.close('all')

# Global variable declaration
K = None


# ODE equations
def f(t, x):
    global K
    dxdt = K * x
    return dxdt


# Initial time
t0 = 0

# Initial condition
x0 = 10
x1 = []
tf = 2

# ODE solver options
# In scipy, these are mapped to solve_ivp parameters
initial_step = 0.001
max_step = 0.1

for i in range(1, 501):  # 1 to 500 inclusive
    K = -4 + 2 * np.random.rand()
    
    # Solve ODE using RK23 method (equivalent to ode23)
    sol = solve_ivp(f, [t0, tf], [x0], method='RK23', 
                    first_step=initial_step, max_step=max_step)
    
    # Extract final value
    x1.append(sol.y[0, -1])

# Plot histogram
plt.figure()
plt.hist(x1)
plt.title(f'Histogramme de x({tf})')
plt.show()
