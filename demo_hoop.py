
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

import tkinter as tk

def on_button_click():
    root.quit()  # Ends the mainloop and continues the script

root = tk.Tk()


button = tk.Button(root, text="Continue", command=on_button_click)
button.pack(padx=50, pady=20)

# Clear all variables (Python starts fresh each run, but for completeness)
# close all figures
plt.close('all')

# Global variables
phi = 1


## system parameters
m = 1
g = 9.8
l = 1
k = 0
omega2 = g / l


## simulation parameters
theta0=1
thetap0=0
tf = 8


animation=1
speed=0.01 ## animation speed


def f2(t, y):
    """
    Differential equation system for the hoop pendulum
    
    Parameters:
    t : float
        Time
    y : array-like
        State vector [position, velocity]
    
    Returns:
    dydt : list
        Derivatives [velocity, acceleration]
    """
    global m
    global g
    global l
    global omega2
    global k
    global u
    
    # y[0]: position (theta)
    # y[1]: speed (theta_dot)
    dydt = [y[1], -g/l*(np.sin(y[0])) - k/m*y[1] + u*u*np.cos(y[0])*np.sin(y[0])]  # ma = -mg
    
    return dydt


def pendule(theta, time, fig_num, title_str, fontsize):
    """
    Pendule animation function
    
    NOTE: This is a placeholder implementation. You need to replace this with your actual
    pendule visualization function. This function should visualize the pendulum at 
    the given angle theta at the specified time.
    
    Parameters:
    theta : float
        Angular position of the pendulum
    time : float
        Current time
    fig_num : int
        Figure number
    title_str : str
        Title string for the plot
    fontsize : int
        Font size for text
    """
    global l
    
    plt.figure(fig_num)
    plt.clf()
    
    # Calculate pendulum bob position
    x = l * np.sin(theta)
    y = -l * np.cos(theta)
    
    # Plot the pendulum
    plt.plot([0, x], [0, y], 'b-', linewidth=2)
    plt.plot(x, y, 'ro', markersize=10)
    plt.plot(0, 0, 'ko', markersize=5)
    
    # Set plot properties
    plt.xlim([-1.5*l, 1.5*l])
    plt.ylim([-1.5*l, 0.5*l])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'{title_str}, t={time:.2f}s', fontsize=fontsize)
    plt.grid(True)
    
    plt.draw()
    plt.pause(0.01)




fontsize = 20


# Main loop through different values of u
for u in [1, 2, 3, 3.5, 4, 5, 6]:
    theta = theta0
    thetap = thetap0
    
    # thetap = sqrt(2*omega2*(1+cos(theta)))
    x0 = [theta, thetap]
    
    ### NONLINEAR CASE
    
    # Solve the ODE using solve_ivp (similar to MATLAB's ode23)
    sol = solve_ivp(f2, [0, tf], x0, method='RK23', dense_output=True, max_step=0.1)
    
    # Extract solution
    t = sol.t
    ynl = sol.y.T  # Transpose to match MATLAB's output format (rows are time points)
    
    # Note: MATLAB's ode23 with events returns te, ye, ie for event detection
    # If events are needed, add events parameter to solve_ivp
    te = []
    ye = []
    ie = []
    
    if animation:
        # Create/get figure 1
        fig = plt.figure(1)
        

        try:
            mngr = plt.get_current_fig_manager()
            # Set window position and size
            # coordf format: [left, bottom, width, height]
            mngr.window.setGeometry(coordf[0], coordf[1], coordf[2], coordf[3])
        except:
            # If window manager doesn't support setGeometry, try alternative
            try:
                fig.canvas.manager.window.wm_geometry(f"{coordf[2]}x{coordf[3]}+{coordf[0]}+{coordf[1]}")
            except:
                # If that also fails, just continue without setting window size
                pass
        
        # Animate the pendulum
        for j in range(0, len(t), max(1, round(len(t)*speed/1000))):
            pendule(ynl[j, 0], t[j], 1, f'HOOP  u={u}', fontsize)
            
            # Set figure position again (in case it was changed)
            try:
                mngr = plt.get_current_fig_manager()
                mngr.window.setGeometry(coordf[0], coordf[1], coordf[2], coordf[3])
            except:
                try:
                    fig.canvas.manager.window.wm_geometry(f"{coordf[2]}x{coordf[3]}+{coordf[0]}+{coordf[1]}")
                except:
                    pass
    
    # Pause - wait for user input before continuing to next iteration
    #input("Press Enter to continue...")

  
    # Pause here until the button is clicked
    root.mainloop()

   
