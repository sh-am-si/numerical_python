import scipy.special as sp
import matplotlib.pylab as plt
import numpy as np

num = 7
max_val = 20

root_set = set.union(*[{r for r in sp.jn_zeros(n=n, nt=round(max_val)) if r < max_val} for n in range(num)])

arg = np.linspace(0, max_val, 10000)
for i in range(num):
    plt.plot(arg, sp.jn(i, arg), label='$J_{' + str(i) + '}(x)$')
    plt.scatter(list(root_set), np.zeros(len(root_set)), c='k', s=4)

plt.xlim([0, max_val])
plt.ylim([-0.5, 1])
plt.legend()
plt.show()
