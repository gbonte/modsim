

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import matplotlib
matplotlib.use('TkAgg')  # Switch backend

sigma = 10
r = 28
b = 2.66

tf = 100
x0 = [-3.3178, -5.2182, 18.7739]


def f(t, x):
    """
    Lorenz system differential equations
    """
    global sigma
    global r
    global b
    
    dxdt = np.array([
        -sigma*x[0] + sigma*x[1],
        -x[0]*x[2] + r*x[0] - x[1],
        x[0]*x[1] - b*x[2]
    ])
    
    return dxdt


# Solve ODE using RK23 method (equivalent to Matlab's ode23)
sol = solve_ivp(f, [0, tf], x0, method='RK23', dense_output=True, 
                events=None, max_step=np.inf)

# Extract time and solution arrays
t = sol.t
x = sol.y.T  # Transpose to match Matlab's output format (rows are time points, columns are variables)

# Store event information (matching Matlab's ode23 output structure)
te = []
ye = []
ie = []





# Animated 3D plot with interactive rotation capability
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+900+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)

for i in range(0, x.shape[0], 20):
    ax.clear()
    ax.plot3D(x[0:i+1, 0], x[0:i+1, 1], x[0:i+1, 2])

    ax.view_init(elev=30, azim=30)
    plt.pause(0.001)

# Keep the final plot open and interactive (rotatable with mouse)
plt.show()


