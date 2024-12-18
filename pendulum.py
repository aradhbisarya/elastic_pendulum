import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


N = 1000
T = 100
dt = T/N
t = np.linspace(0,T,N)

# Parameters

k = 30 # VARY
m = 1 # VARY
g = 10 # FIXED
l = 1 # FIXED

print(" r at equilibrium = {}".format(l + m*g/k))
print(" w_1 = {} w_2 = {}".format(np.sqrt(k/m), np.sqrt(g/(l+m*g/k))))

# calculating slope

def slope(x):
    r,rd,th,thd = x
    return(np.array([rd, r*thd**2 +g*np.cos(th) -k*(r-l)/m, thd, -g*np.sin(th)/r -2*rd*thd/r]))

# Initial conditions
#[r, r_dot, theta, theta_dot]

x = [np.array([l+m*g/k,0,0,1])]

for i in range(N-1): #Runge Kutta stepwise increase
    k1 = slope(x[i])
    k2 = slope(x[i]+0.5*dt*k1)
    k3 = slope(x[i]+0.5*dt*k2)
    k4 = slope(x[i]+dt*k3)

    x.append(x[i]+dt*(k1+2*k2+2*k3+k4)/6)

x = np.array(x)
fig,((ax1,ax3),(ax2,ax4)) = plt.subplots(2,2)

ax1.set_title("r")
ax1.plot(t,x[:,0])

ax2.set_title("theta")
ax2.plot(t,x[:,2])

#Plotting Energies
K1 = 0.5*m*x[:,1]**2
V1 = 0.5*k*(x[:,0]-l)**2

K2 = 0.5*m*x[:,0]**2*x[:,3]**2
V2 = -m*g*x[:,0]*np.cos(x[:,2])
ax4.plot(t, K1+V1+K2+V2)
ax4.plot(t,K1+V1)
ax4.plot(t,K2+V2)
ax4.legend(["Total Energy", "spring Energy", "Pendulum Energy"])

ax3.set_xlim([-3,3])
ax3.set_ylim([-2,0])
r,rd,th,thd = x[0]

pendulum = ax3.scatter(r*np.sin(th),-r*np.cos(th))
spring = ax3.plot([0,r*np.sin(th)],[0,-r*np.cos(th)])[0]

def update(frame):
    # for each frame, update the data stored on each artist.
    r,rd,th,thd = x[frame]

    pendulum.set_offsets([r*np.sin(th),-r*np.cos(th)])
    spring.set_xdata([0,r*np.sin(th)])
    spring.set_ydata([0,-r*np.cos(th)])
    return (pendulum)

ani = animation.FuncAnimation(fig=fig, func=update, frames=N, interval=90)
plt.show()
ani.save("pendulum_animation_multi_mode.gif")
