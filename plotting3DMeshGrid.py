# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:27:26 2022

@author: ahaber
"""

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

# demonstration 

x=np.linspace(0,5,6)
y=np.linspace(0,5,6)

X, Y = np.meshgrid(x,y)

X[0,:]
Y[0,:]

for pair in zip(X[0,:],Y[0,:]):
    print(pair)


# plotting
x=np.linspace(-5,5,11)
y=np.linspace(-5,5,11)

X, Y = np.meshgrid(x,y)

Z= X**2+Y**2

fig=plt.figure()
plt.contourf(X,Y,Z,cmap='plasma')
plt.axis('scaled')
plt.colorbar()
plt.savefig('contour1.png')
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap="plasma", linewidth=0, antialiased=False, alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
# rotation
ax.view_init(30, 60)
plt.savefig('3Dplot1.png',dpi=600)
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.view_init(30, 60)
plt.savefig('3Dplot2.png',dpi=600)
plt.show()




