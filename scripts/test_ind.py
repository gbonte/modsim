import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Switch backend
# clear all, close all
plt.close('all')

def clamp01(x):
    "Clamp a float to [0, 1]."
    return max(0.005, min(0.995, float(x)))

np.random.seed(0)
N = 700
D2 = [0.5]

for i in range(1, N):
    if i % 3 == 0:
        D2.append(np.random.rand())
    else:
        D2.append(clamp01(0.65*D2[i-1]+0.35*float(np.random.rand(1))))

D2 = np.array(D2)
D = np.random.rand(N, 1).flatten()


Xlim = [-5, 5]

# figure(1)
fig1 = plt.figure(1)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+100+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)


L = plt.plot(range(1, N+1), D, 'o',  markersize=5)

plt.ylim([0.2, 0.8])
plt.xlabel('i')
plt.ylabel('x_i')
plt.title("Random sequence 1")


# figure(2)
fig2 = plt.figure(2)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+100+600")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)


plt.plot(range(1, N+1), D2, 'o',  markersize=5)
plt.ylim([0.2, 0.8])
plt.gca().tick_params(labelsize=24)
plt.xlabel('i')
plt.ylabel('x_i')
plt.title("Random sequence 2")
plt.show(block=False)
input("Type to continue")

fig3 = plt.figure(3)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+800+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)


plt.plot(D[0], D[1], 'o', markersize=5)

for i in range(N-1):
    plt.plot(D[i], D[i+1], 'ko', markersize=5)
plt.xlabel('x_i')
plt.ylabel('x_{i+1}')
plt.title("Correlation random sequence 1")


# figure(2)
fig4 = plt.figure(4)

manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+800+600")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)


plt.plot(D2[0], D2[1], 'ko', markersize=5)

for i in range(N-1):
    plt.plot(D2[i], D2[i+1], 'ko', markersize=5)
plt.xlabel('x_i')
plt.ylabel('x_{i+1}')
plt.title("Correlation random sequence 2")


plt.show()
