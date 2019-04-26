# http://www.scipy-lectures.org/advanced/image_processing/
# http://scikit-image.org/docs/dev/user_guide/numpy_images.html

import matplotlib.image
import matplotlib.pylab as plt
import numpy as np
import matplotlib

# matplotlib.rcParams["savefig.directory"] = 'C:\Volodya\Introduction2Python\PyCourse\ip\\'

biedronka = matplotlib.image.imread('biedronka.png')

print(type(biedronka))
print(biedronka.shape)
print(biedronka.dtype)
print('red:', np.average(biedronka[:, :, 0]))
print('green:', np.average(biedronka[:, :, 1]))
print('blue:', np.average(biedronka[:, :, 2]))
# print('alpha:', np.average(jb[:, :, 3]))

plt.figure()
plt.imshow(biedronka)
plt.draw()

plt.figure()
plt.hist(biedronka[:, :, 0].ravel(), 256, [0, 1], color='r')
plt.xlim(0, 1)
plt.draw()
plt.figure()
plt.hist(biedronka[:, :, 1].ravel(), 256, [0, 1], color='g')
plt.xlim(0, 1)
plt.draw()
plt.figure()
plt.hist(biedronka[:, :, 2].ravel(), 256, [0, 1], color='b')
plt.xlim(0, 1)
plt.draw()

plt.figure()
plt.hist(biedronka[:, :, 0].ravel(), 256, [0, 1], alpha=0.5, color='r')
plt.hist(biedronka[:, :, 1].ravel(), 256, [0, 1], alpha=0.5, color='g')
plt.hist(biedronka[:, :, 2].ravel(), 256, [0, 1], alpha=0.5, color='b')
plt.xlim(0, 1)

plt.draw()
plt.show()



