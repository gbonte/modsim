
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.patches import Circle
import warnings

import matplotlib
matplotlib.use('TkAgg')  # Switch backend

# clear all
# close all
plt.close('all')

phi = 1
u = 0
animation = 1

# Global variables
m = 1
g = 9.8
l = 1
k = 0
omega2 = g/l
speed=2.5
tf = 4
Fsize = 15
def f(y, t):
    """
    Linear pendulum ODE
    y1: position
    y2: speed
    """
    # dydt = [y(2); -g/l*(y(1))-k/m*y(2)]; % ma =-mg
    dydt = [y[1], -g/l*(y[0])-k/m*y[1]]
    return dydt


def f2(y, t):
    """
    Non-linear pendulum ODE
    y1: position
    y2: speed
    """
    # dydt = [y(2); -g/l*(sin(y(1)))-k/m*y(2)]; % ma =-mg
    dydt = [y[1], -g/l*(np.sin(y[0]))-k/m*y[1]]
    return dydt


def pendule(angle, time, fig_num, title_str, fontsize):
    """
    Placeholder for pendulum animation function
    This function is called but not defined in the original MATLAB code
    
    Expected behavior: Draw a pendulum at given angle
    Parameters:
    - angle: pendulum angle
    - time: current time
    - fig_num: figure number
    - title_str: title string
    - fontsize: font size
    """
    plt.figure(fig_num)
    plt.clf()
    
    # Draw pendulum (basic implementation)
    x_pend = [0, l*np.sin(angle)]
    y_pend = [0, -l*np.cos(angle)]
    
    plt.plot(x_pend, y_pend, 'k-', linewidth=3)
    plt.plot(x_pend[1], y_pend[1], 'ro', markersize=20)
    plt.plot(0, 0, 'ko', markersize=10)
   
    
    plt.axis('equal')
    plt.xlim([-2*l, 2*l])
    plt.ylim([-2*l, 2*l])
    plt.title(title_str, fontsize=fontsize)
    plt.text(0, 0.3*l, f't = {time:.2f}s', fontsize=fontsize, ha='center')
    plt.grid(True)
    
    plt.draw()
    
    plt.pause(0.01)



xrange = [-10, 10]
yrange = [-10, 10]
x, y = np.meshgrid(np.arange(xrange[0], xrange[1]+0.5, 0.25), 
                    np.arange(yrange[0], yrange[1]+0.5, 0.25))
xp = y
yp = -g/l*(x)-k/m*y
yp2 = -g/l*np.sin(x)-k/m*y

coordf1 = [10, 743, 859, 601]
coordf2 = [10, 75, 862, 574]
coordf3 = [889, 740, 683, 599]
coordf4 = [889, 85, 683, 599]

coordf1 = [1, 568, 648, 422]
coordf2 = [1, 68, 648, 392]
coordf3 = [657, 566, 591, 422]
coordf4 = [657, 68, 591, 392]

# Create figures
fig1 = plt.figure(1)
# Convert MATLAB position [left, bottom, width, height] to inches (approximate)
# MATLAB uses pixels, matplotlib uses inches
dpi = 100
fig1.set_size_inches(coordf1[2]/dpi, coordf1[3]/dpi)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+900+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)



fig2 = plt.figure(2)
fig2.set_size_inches(coordf2[2]/dpi, coordf2[3]/dpi)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+900+800")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)



fig3 = plt.figure(3)
fig3.set_size_inches(coordf3[2]/dpi, coordf3[3]/dpi)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+200+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)

fig4 = plt.figure(4)
fig4.set_size_inches(coordf4[2]/dpi, coordf4[3]/dpi)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+200+800")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)

plt.figure(1)

sc=35
arrow = np.sqrt(xp**2 + yp**2)

plt.quiver(x, y, xp/arrow, yp/arrow, scale=sc)
plt.xlim([-5, 5])
plt.ylim([-10, 10])

plt.title(' lineaire', fontsize=Fsize)
ax1 = plt.gca()
ax1.tick_params(labelsize=Fsize)
plt.hold = True  # hold on

plt.figure(2)

arrow = np.sqrt(xp**2 + yp2**2)
plt.xlim([-5, 5])
plt.ylim([-10, 10])
plt.quiver(x, y, xp/arrow, yp2/arrow, color='r', scale=sc)
plt.xlim([-5, 5])
plt.ylim([-10, 10])
plt.title(' non lineaire', fontsize=Fsize)
ax2 = plt.gca()
ax2.tick_params(labelsize=Fsize)
plt.hold = True  # hold on


for thetap in [2, 3, 6.5, 9, 10,12]:
    theta = 0
    
    # thetap=sqrt(2*omega2*(1+cos(theta)))
    x0 = [theta, thetap]
    t = np.linspace(0, tf, 1000)
    y_sol = odeint(f, x0, t)
    
    # subplot(1,2,1); plot(t,y(:,1),'-'); xlabel('t'); ylabel('x_1');hold on
    # subplot(1,2,2); plot(t,y(:,2),'-'); xlabel('t'); ylabel('x_2');hold on
    
    
    
    if animation:
        plt.figure(3)
        
        for j in range(0, len(t), max(1, round(len(t)*speed/100))):
            pendule(y_sol[j, 0], t[j], 3, f' LINEAIRE: Acc(0)={thetap}', Fsize)

    plt.figure(1)
    plt.xlim([-5, 5])
    plt.ylim([-10, 10])
    plt.plot(x0[0], x0[1], 'ko', linewidth=2)
    plt.plot(y_sol[:, 0], y_sol[:, 1], 'k-', linewidth=2)
    
    plt.xlabel('x_1', fontsize=Fsize)
    plt.ylabel('x_2', fontsize=Fsize)
    
    plt.pause(0.1)

    
    ### NON LINEAIRE
    
    ynl = odeint(f2, x0, t)
    
    
    if animation:
        plt.figure(4)
        
        for j in range(0, len(t), max(1, round(len(t)*speed/100))):
            pendule(ynl[j, 0], t[j], 4, f' NON LINEAIRE Acc(0)={thetap}', Fsize)
    
    plt.pause(0.1)
    plt.figure(2)
    plt.xlim([-5, 5])
    plt.ylim([-10, 10])
    plt.plot(x0[0], x0[1], 'ko', linewidth=2)
    plt.plot(ynl[:, 0], ynl[:, 1], 'k-', linewidth=2)
    plt.title(' non lineaire', fontsize=Fsize)
    plt.xlabel('x_1', fontsize=Fsize)
    plt.ylabel('x_2', fontsize=Fsize)
    
  


plt.show()

