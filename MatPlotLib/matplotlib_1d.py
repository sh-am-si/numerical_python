import numpy as np
import matplotlib.pylab as plt

arg = np.linspace(0, 2 * np.pi, 200)

plt.title('Trigonometric functions')
plt.plot(arg, np.sin(arg), c='r', lw=2, ls='--',
          label=r'$\sin(x)$') # modified line
plt.plot(arg, np.cos(arg), c='g', lw=3, ls='-.',
         label=r'$\cos(x)$') # modified line
plt.legend()
plt.show()     
