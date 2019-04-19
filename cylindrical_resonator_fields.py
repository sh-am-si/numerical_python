import scipy.special as sp
import matplotlib.pylab as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D


def draw_field(m, n, k, ax=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    r = np.linspace(0, 1, 100)
    p = np.linspace(0, 2 * np.pi, 100)
    R, P = np.meshgrid(r, p)
    Z = sp.jn(m, k * R) * np.exp(1j * n * P)

    # Express the mesh in the cartesian system.
    X, Y = R * np.cos(P), R * np.sin(P)
    ax.plot_surface(X, Y, np.real(Z), cmap=plt.cm.jet)
    plt.draw()


def draw_contour(m, n, k, ax=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)

    r = np.linspace(0, 1, 100)
    p = np.linspace(0, 2 * np.pi, 100)
    R, P = np.meshgrid(r, p)
    Z = sp.jn(m, k * R) * np.exp(1j * n * P)

    # Express the mesh in the cartesian system.
    X, Y = R * np.cos(P), R * np.sin(P)
    ax.contourf(X, Y, np.real(Z), 60, cmap=plt.cm.jet)
    plt.draw()


if __name__ == '__main__':
    m, n = 2, 3
    root = sp.jn_zeros(n=m, nt=n)[-1]
    draw_field(m, n, root)
    draw_contour(m, n, root)
    plt.show()
