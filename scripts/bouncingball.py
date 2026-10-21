import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Dynamics: y[0] = position, y[1] = velocity
def f(t, y):
    return [y[1], -9.8]

# Event: detect when ball hits the ground (height = 0)
def hit_ground(t, y):
    return y[0]
hit_ground.terminal = True
hit_ground.direction = -1

# Circle drawing helper
def draw_circle(center, radius,color="red"):
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    plt.fill(x, y, color=color)  

# Initial conditions
t_start = 0
t_final = 500
y0 = [20, -2]
tout = [t_start]
yout = [y0]
teout, yeout, ieout = [], [], []

plt.figure()
plt.xlim(0, 30)
plt.ylim(0, 25)
plt.box(True)

for i in range(20):
    sol = solve_ivp(f, [t_start, t_final], y0, events=hit_ground,
                    max_step=0.05, rtol=1e-6, atol=1e-9)

    t = sol.t
    y = sol.y.T
    nt = len(t)

    tout.extend(t[1:])
    yout.extend(y[1:])
    if sol.t_events[0].size > 0:
        teout.append(sol.t_events[0][0])
        yeout.append(sol.y_events[0][0])
        ieout.append(1)

    # Update initial conditions with bounce
    y0 = [0, -0.9 * y[-1][1]]
    t_start = t[-1]

    # Animate ball
    for tt in range(nt):
        plt.clf()
        draw_circle([10, y[tt][0] + 1], 1)
        plt.axis([0, 20, 0, 20])
        if tt > 0:
            plt.pause(0.0001 * (t[tt] - t[tt - 1]))

plt.ylabel('Height')
plt.title('Ball trajectory')
plt.show()