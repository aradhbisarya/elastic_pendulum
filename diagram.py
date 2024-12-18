import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
fig = plt.figure()
plt.xlim([-3,3])
plt.ylim([-7,1])
plt.xticks([])
plt.yticks([])
plt.plot([-2,2],[0,0], "k")

theta_max = 61
theta = np.linspace(1.5, theta_max, 10000)
x = []
y = []
for th in theta:
    x.append(0.2+ 0.02*th - 0.1*np.cos(th))
    y.append(-0.6 - 0.04*th + 0.15*np.sin(th))
plt.plot(x,y, 'k')
plt.plot([0,0.2],[0,-0.5], 'k')
plt.plot([1.5],[-3.3], 'ok', ms = 12)
plt.plot([0,0],[0,-5],"--k")
plt.text(1.65,-3.4,'m')
plt.text(1,-1.6,'k,l')
plt.text(0.16,-1.35,r'$\theta$')

plt.plot([0,-2],[0,-1],"-.k")
plt.plot([1.5,-0.5],[-3.3,-4.3],"-.k")

plt.arrow(-2,-1,1.5,-3.3)
plt.text(-1.4,-3,'r')

ax = plt.gca()
ax.add_patch(patch.Arc([0,0],2,2, theta1=270, theta2=299))
plt.show()
