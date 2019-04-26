import numpy as np
import matplotlib.pylab as plt
import scipy.special as sp

num = 100

x = np.linspace(start=-2, stop=2, num=num)
y = np.linspace(start=-2, stop=2, num=num)

X, Y = np.meshgrid(x, y)
Z = np.ndarray(X.shape, dtype=complex)

ro = np.sqrt(X ** 2 + Y ** 2)
phi = np.arctan2(Y, X)
m = 4
k = 14.3
Z = sp.jv(m, k * ro) * np.exp(1j * m * phi)

fig = plt.figure()
[ax1, ax2], [ax3, ax4] = fig.subplots(nrows=2, ncols=2)

ax1.set_title('real part')
im1 = ax1.contourf(X, Y, np.real(Z), num, cmap=plt.cm.jet)
ax1.set_aspect('equal')
fig.colorbar(im1, ax=ax1)

ax2.set_title('imaginary part')
im2 = ax2.contourf(X, Y, np.imag(Z), num, cmap=plt.cm.jet)
ax2.set_aspect('equal')
fig.colorbar(im2, ax=ax2)

ax3.set_title('absolute value')
im3 = ax3.contourf(X, Y, np.abs(Z), num, cmap=plt.cm.jet)
ax3.set_aspect('equal')
fig.colorbar(im3, ax=ax3)

ax4.set_title('phase')
im4 = ax4.contourf(X, Y, np.angle(Z), num, cmap=plt.cm.jet)
ax4.set_aspect('equal')
fig.colorbar(im4, ax=ax4)

# plt.aspect('equal')
plt.show()
