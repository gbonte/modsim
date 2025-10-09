
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')  # Switch backend

# clear all
plt.close('all')

def logi(x, a):
    """
    Logistic map function
    """
    f = a * x * (1 - x)
    return f

X = np.arange(0, 1.01, 0.01)
import tkinter as tk

def on_button_click():
    root.quit()  # Ends the mainloop and continues the script

root = tk.Tk()


button = tk.Button(root, text="Continue", command=on_button_click)
button.pack(padx=50, pady=20)


import sys

if len(sys.argv) > 1:
    a = float(sys.argv[1])
else:
    a=1.0 

print(a)

if (a < 0):
    raise Exception("valeur de a non admissible")

if (a > 4):
    raise Exception("valeur de a non admissible")


f = plt.figure(1)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+900+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(800, 550)


pl = plt.plot(X, logi(X, a))
plt.setp(pl, linewidth=2)
plt.gca().tick_params(labelsize=28)
plt.hold = True  # This is implicit in newer matplotlib versions
pl2 = plt.plot(X, X, 'r')
plt.setp(pl2, linewidth=2)


fsize=14
x = 1 - 0.05
xx = x - 0.005

xk = []
xxk = []

for i in range(1, 501):  # MATLAB's 1:500 translates to range(1, 501)
    plt.gca().tick_params(labelsize=28)
    
   
    xk.append(x)
    xxk.append(xx)
    
    xn = logi(x, a)
    xxn = logi(xx, a)
    
    plt.figure(1)
    if (i == 1):
        L = plt.plot([x, x], [0, xn], 'b-')
        plt.setp(L, linewidth=2)
    else:
        L = plt.plot([x, x], [x, xn], 'b-')
        plt.setp(L, linewidth=2)
    
    L = plt.plot([x, xn], [xn, xn], 'b-')
    plt.setp(L, linewidth=2)
    
    plt.gca().tick_params(labelsize=fsize)
    plt.xlabel('x(k)', fontsize=fsize)
    plt.ylabel('x(k+1)', fontsize=fsize)
    
    if (a > 1):
        plt.title('a=' + str(a) + ' ; x_{eq}=' + str(0) + ' ; x_{eq}=' + str((a-1)/a), fontsize=fsize)
    else:
        plt.title('a=' + str(a) + ' ; x_{eq}=' + str(0), fontsize=fsize)
    
    x = xn
    xx = xxn
    
    f2 = plt.figure(2)
    # Set position for figure 2

    manager=plt.currentmanager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+900+700")  # X=400 pixels from left, Y=200 pixels from top
    manager.resize(800, 550)    
    plt.clf()  # Clear figure to redraw
    pl3 = plt.plot(xk)

    
    plt.title('x(' + str(len(xk)) + ')=' + str(xk[len(xk)-1]), fontsize=fsize)
    plt.xlabel('k', fontsize=fsize)
    plt.ylabel('x(k)', fontsize=fsize)
    plt.gca().tick_params(labelsize=fsize)
    # hold on is implicit
    plt.plot(xxk, 'r-')
    plt.setp(pl3, linewidth=3)
    
    if i > 2 and a > 3.6:
        f3 = plt.figure(3)
        # Set position for figure 3
        f3.set_size_inches(pf3[2]/dpi, pf3[3]/dpi)
        try:
            f3.canvas.manager.window.wm_geometry("+%d+%d" % (pf3[0], pf3[1]))
        except:
            pass  # Some backends may not support positioning
        
        # hold on is implicit - no need to clear
        pl4 = plt.plot(xk[len(xk)-2], xk[len(xk)-1], '*')
        plt.setp(pl4, markersize=12)
        plt.xlabel('x(k-1)', fontsize=fsize)
        plt.ylabel('x(k+1)', fontsize=fsize)
        plt.gca().tick_params(labelsize=fsize)
    
    plt.pause(0.001)  # Small pause to update figures
    # Wait for user input to continue
        # Pause here until the button is clicked
    root.mainloop()
    


