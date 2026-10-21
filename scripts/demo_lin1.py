
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Clear all variables, close all figures
plt.close('all')

# Global variable
k = None


## ODE equations
def f(t, x):
    """ODE function: dx/dt = k*x"""
    global k
    dxdt = k * x
    return dxdt


# ODE solver options
# Note: scipy's solve_ivp uses different parameter names
# InitialStep -> first_step, MaxStep -> max_step
solver_options = {
    'first_step': 0.001,
    'max_step': 0.01
}

# Initial and final time
t0 = 0    # initial time
tf = 10   # final time
dt = 0.1

# Create figure
fig = plt.figure(1, figsize=(11, 9))
pos = [1, 30, 1100, 900]
# Note: matplotlib uses inches for figsize, position in pixels is set differently
# The figsize above approximates the Matlab position

# Initial condition
x0 = 10

# Solve and plot for k = -1/2
k = -1/2
t_eval = np.arange(t0, tf + dt, dt)
sol = solve_ivp(f, [t0, tf], [x0], method='RK23', t_eval=t_eval, 
                first_step=solver_options['first_step'], 
                max_step=solver_options['max_step'])
t = sol.t
x = sol.y[0]
plt.plot(t, x, '-', linewidth=2)
plt.hold = True  # Note: hold is deprecated in newer matplotlib, plots overlay by default

# Solve and plot for k = -1
k = -1
sol = solve_ivp(f, [t0, tf], [x0], method='RK23', t_eval=t_eval,
                first_step=solver_options['first_step'], 
                max_step=solver_options['max_step'])
t = sol.t
x = sol.y[0]
plt.plot(t, x, '-', linewidth=2)

# Solve and plot for k = -2
k = -2
sol = solve_ivp(f, [t0, tf], [x0], method='RK23', t_eval=t_eval,
                first_step=solver_options['first_step'], 
                max_step=solver_options['max_step'])
t = sol.t
x = sol.y[0]
plt.plot(t, x, '-', linewidth=2)

# Solve and plot for k = -4
k = -4
sol = solve_ivp(f, [t0, tf], [x0], method='RK23', t_eval=t_eval,
                first_step=solver_options['first_step'], 
                max_step=solver_options['max_step'])
t = sol.t
x = sol.y[0]
plt.plot(t, x, '-', linewidth=2)

# Add title and labels
plt.title("Ordre 1: x'=kx")
plt.xlabel('t')
plt.ylabel('x')

# Add legend
h = plt.legend(["k=-1/2  T=8", "k=-1    T=4 ",
                "k=-2    T=2", "k=-4    T=1"])

# Set font sizes
ax = plt.gca()
ax.tick_params(axis='both', labelsize=24)
plt.setp(h.get_texts(), fontsize=24)

# Show the plot (equivalent to pause in interactive mode)
plt.show()

