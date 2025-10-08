
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

import matplotlib
matplotlib.use('TkAgg')  # Switch backend

plt.close('all')

# -2,1
# -1, -2 
# -2, -1
lam1 = -0.1

lam2 = 0.2

# initial condition
x0 = np.array([1, 0])
# first eigenvector is directed as V(:,1)
# second eigenvector is as V(:,2)
V = np.array([[0.5, 1], [1, -1]])
# V=[2,1;2,1] 

c = np.linalg.solve(V, x0)

a = c[0]
b = c[1]
# initial condition on eigenvector 1 (x2=x1)
x0A = a * V[:, 0]
# initial condition on eigenvector 2 (x2=-x1)
x0B = b * V[:, 1]

# 
# x0=x0A+x0B

# Define global variable A
A = None

def f2(t, x):
    global A
    dxdt = A @ x
    return dxdt

# get(figure(1),"Position")
fig = plt.figure(1)

manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+900+100")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(900, 600)


D = np.diag([lam1, lam2])

# matrix with eigenvectors V and eigenvalues D
# eig(A) check on eigenvalues
A = V @ D @ np.linalg.inv(V)

tf = 10
T = np.arange(0, tf + 0.01, 0.01)

# Solve ODE for x0A
sol_A = solve_ivp(f2, [0, tf], x0A, method='RK23', t_eval=T)
t = sol_A.t
xA_temp = sol_A.y.T
# Interpolate to ensure we have values at all T points
if len(t) != len(T):
    interp_func_xA0 = interp1d(t, xA_temp[:, 0], kind='linear', fill_value='extrapolate')
    interp_func_xA1 = interp1d(t, xA_temp[:, 1], kind='linear', fill_value='extrapolate')
    xA = np.column_stack((interp_func_xA0(T), interp_func_xA1(T)))
else:
    xA = xA_temp

# Solve ODE for x0B
sol_B = solve_ivp(f2, [0, tf], x0B, method='RK23', t_eval=T)
t = sol_B.t
xB_temp = sol_B.y.T
# Interpolate to ensure we have values at all T points
if len(t) != len(T):
    interp_func_xB0 = interp1d(t, xB_temp[:, 0], kind='linear', fill_value='extrapolate')
    interp_func_xB1 = interp1d(t, xB_temp[:, 1], kind='linear', fill_value='extrapolate')
    xB = np.column_stack((interp_func_xB0(T), interp_func_xB1(T)))
else:
    xB = xB_temp

# Solve ODE for x0
sol = solve_ivp(f2, [0, tf], x0, method='RK23', t_eval=T)
t = sol.t
x_temp = sol.y.T
# Interpolate to ensure we have values at all T points
if len(t) != len(T):
    interp_func_x0 = interp1d(t, x_temp[:, 0], kind='linear', fill_value='extrapolate')
    interp_func_x1 = interp1d(t, x_temp[:, 1], kind='linear', fill_value='extrapolate')
    x = np.column_stack((interp_func_x0(T), interp_func_x1(T)))
else:
    x = x_temp

N = x.shape[0]

xx = np.arange(-10, 11, 1)




plt.plot(xx, V[1, 0]/V[0, 0]*xx)
plt.hold = True  #
plt.plot(xx, V[1, 1]/V[0, 1]*xx)

mksize=7

for i in range(0, N, 5):

    I = i
    
    if lam1 > 0:
        plt.plot(xA[I, 0], xA[I, 1], 'r*', linewidth=4, markersize=mksize)
    else:
        plt.plot(xA[I, 0], xA[I, 1], 'g*', linewidth=4, markersize=mksize)
    
    if lam2 > 0:
        plt.plot(xB[I, 0], xB[I, 1], 'r*', linewidth=4, markersize=mksize)
    else:
        plt.plot(xB[I, 0], xB[I, 1], 'g*', linewidth=4, markersize=mksize)
    
    plt.plot(x[I, 0], x[I, 1], 'k*', linewidth=3, markersize=mksize)
    
    # Format the title
    title_str = (f't={t[i]:.3g};   x=[{x[i, 0]:.3g} {x[i, 1]:.3g}]=   '
                 f'[{xA[i, 0]:.3g} {xA[i, 1]:.3g}]+ '
                 f'[{xB[i, 0]:.3g} {xB[i, 1]:.3g}]')
    plt.title(title_str)
    
    if (lam1 < 0 and lam2 < 0):
        plt.axis([-0.25, 1.1, -1, 1])
    else:
        plt.axis([-1, 5, -3, 3])
    
    ax = plt.gca()
    ax.tick_params(labelsize=24)
    
    # Format the xlabel
    xlabel_str = (f'v1=[{V[0, 0]}, {V[1, 0]}], '
                  f'v2=[{V[0, 1]}, {V[1, 1]}]; '
                  f'lam1={lam1}, lam2={lam2}')
    plt.xlabel(xlabel_str)
    
    # set(figure(1),"Position",pos);
    xt = ax.get_xticks()
    
    plt.pause(0.15)
 

