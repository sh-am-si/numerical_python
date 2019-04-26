# http://www.scipy-lectures.org/advanced/image_processing/
# http://scikit-image.org/docs/dev/user_guide/numpy_images.html

import matplotlib.image
import matplotlib.pylab as plt
import numpy as np
import matplotlib

dir = 'C:\Volodya\Introduction2Python\\NumPyCourse\pics\\'
matplotlib.rcParams["savefig.directory"] = dir

monalisa = matplotlib.image.imread('monalisa.png')

plt.figure('original')
plt.imshow(monalisa)
plt.savefig(dir + 'monalisa_original.png', transparent=True, bbox_inches='tight', pad_inches=0)
plt.draw()

ml = monalisa.copy()  # first way of copying
plt.figure('quarters are blacked and whited')
ml[:ml.shape[0] // 2, :ml.shape[1] // 2, :-1] = 0
ml[ml.shape[0] // 2:, ml.shape[1] // 2:, :-1] = 1
plt.imshow(ml)
plt.savefig(dir + 'monalisa_black_white.png', transparent=True, bbox_inches='tight', pad_inches=0)
plt.draw()

ml = monalisa[:, :, :]  # another way of array copying actually the same as ml = monalisa[:,:,:]
plt.figure('colored')
ml[:ml.shape[0] // 2, :ml.shape[1] // 2, [0, 1]] = 0
ml[ml.shape[0] // 2:, :ml.shape[1] // 2, [0, 2]] = 1
ml[:ml.shape[0] // 2, ml.shape[1] // 2:, [1]] = 1
ml[ml.shape[0] // 2:, ml.shape[1] // 2:, [0, 1]] = 1
plt.imshow(ml)
plt.savefig(dir + 'monalisa_col.png', transparent=True, bbox_inches='tight', pad_inches=0)
plt.draw()

plt.show()
