import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np
import mpl_toolkits
from mpl_toolkits.axes_grid.axislines import SubplotZero

fig=plt.figure(num=1)
ax=SubplotZero(fig,111)
fig.add_subplot(ax)

#ax=fig.add_subplot(111)

def vf(t,x):
    dx=np.zeros(2)
    dx[0]=1
    dx[1]=x[0]/x[1]
    return dx
t0=0; tEnd=10; dt=0.01;
r=ode(vf).set_integrator('vode',method='bdf',max_step=dt)
ic=[[0.2,0.2],[0.2,-0.2],[0.2,-0.5],[0.2,0.7]]
color=['r','b','g','y']

for direction in ["xzero","yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
for k in range(len(ic)):
    Y=[]; T=[]; S=[];
    r.set_initial_value(ic[k],t0).set_f_params()
    while r.successful() and r.t+dt<tEnd:
        r.integrate(r.t+dt)
        Y.append(r.y)

    S=np.array(np.real(Y))
    ax.plot(S[:,0],S[:,1],color=color[k],lw=1.25)

X,Y=np.meshgrid(np.linspace(-5,5,40),np.linspace(-5,5,20))
U=1
V=X/Y

N=np.sqrt(U**2+V**2)
U2,V2=U/N,V/N
ax.quiver(X,Y,U2,V2)

plt.xlim([-5,5])
plt.ylim([-5,5])
plt.ylabel(r"$y$")
plt.show()

    

        

