import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Switch backend

fig_initial = plt.figure()
ax_initial = plt.gca()
ax_initial.tick_params(labelsize=28)
plt.close(fig_initial)

N = 100
R = 20000
mu = 1
muhat = []
muhat2 = []
muhat3 = []

H=R/2

for r in range(R):
    DN = np.random.randn(N) + mu
    muhat.append(np.mean(DN))
    muhat2.append(np.min(DN))
    muhat3.append(DN[0])



##############@

fig1 = plt.figure(1)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+100+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)


plt.clf()

plt.hist(muhat)


L = plt.plot([mu, mu], [0, H], 'r')

plt.setp(L, linewidth=3)

plt.title('Distribution estimateur mean')

##############@

fig2 = plt.figure(2)

manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+800+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)

plt.clf()
plt.hist(muhat2)

L = plt.plot([mu, mu], [0, H], 'r')

plt.setp(L, linewidth=3)
plt.title('Distribution estimateur min')

##############@

fig3 = plt.figure(3)
manager=plt.currentmanager = plt.get_current_fig_manager()
manager.window.wm_geometry("+1500+50")  # X=400 pixels from left, Y=200 pixels from top
manager.resize(600, 450)

plt.clf()
plt.hist(muhat3)

L = plt.plot([mu, mu], [0, H], 'r')
plt.setp(L, linewidth=3)

plt.title('Distribution estimateur first')


plt.show()
