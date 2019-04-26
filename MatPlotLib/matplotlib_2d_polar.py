import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

azimuths = np.linspace(0, 2 * np.pi, 120)
zeniths = np.linspace(0., 5, 120)

r, theta = np.meshgrid(zeniths, azimuths)
# values = np.random.random((azimuths.size, zeniths.size))
values = sp.jv(2, 2 * r) * np.exp(2j * theta)
print(azimuths.shape, zeniths.shape, r.shape, theta.shape, values.shape)

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, np.real(values), cmap=plt.cm.jet)

plt.show()
