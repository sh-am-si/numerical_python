import matplotlib.pylab as plt
import numpy as np


def trigonometrical_function(n):
    if n % 2 == 0:
        return lambda x: np.cos(n // 2 * x), f'$\cos({n // 2}x)$'
    else:
        return lambda x: np.sin(n // 2 * x), f'$\sin({n // 2}x)$'


arg = np.linspace(0, 2 * np.pi, 200)
for n in range(2, 12):
    f, name = trigonometrical_function(n)
    plt.plot(arg, f(arg), label=name)
plt.legend()
plt.show()
