"""
Homogenous dielectric resonator
"""

import matplotlib.pylab as plt
import numpy as np
import scipy.special as sp
import scipy.optimize as opt

def eigenvalues_TM(n=0, m=1, eps=1, r=1):
    return sp.jn_zeros(n=n, nt=m)[-1] / (np.sqrt(eps) * r)


def eigenvalues_TE(n=0, m=1, eps=1, r=1):
    return sp.jnp_zeros(n=n, nt=m)[-1] / (np.sqrt(eps) * r)


def bessel_function_ouput(n=5, m=4, TM=True):
    '''

    :param n: Bessel function order
    :param m: number of the root
    :param TM: True for TM mode, False for TE one
    :return: Latex table of values
    '''
    st = ' m' + ''.join([f' &{i} ' for i in range(n)]) + '\\\\'
    val = lambda _n, _m: eigenvalues_TM(n=_n, m=_m + 1, eps=1, r=1) if TM else eigenvalues_TE(n=_n, m=_m + 1, eps=1,
                                                                                              r=1)
    for _m in range(m):
        st += f'  {_m + 1} ' + ''.join([f'& {round(val(_n, _m), 4)} ' for _n in range(n)]) + '\\\\'
    print(st)


def eigen_function_TM(n, k, eps=10, even=True):
    harmonic = lambda phi: np.cos(phi) if even else np.sin(phi)
    return lambda rho, phi: sp.jn(n, k * np.sqrt(eps)*rho) * harmonic(phi)


def eigen_function_TE(n, k, eps=10, even=True):
    harmonic = lambda phi: np.cos(phi) if even else np.sin(phi)
    return lambda rho, phi: sp.jvp(n, k * np.sqrt(eps)*rho) * harmonic(phi)


def draw_contour(func, rad=1, num=100, ax=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.gca(projection='polar')

    ro = np.linspace(0, rad, num)
    phi = np.linspace(0, 2 * np.pi, num)

    ro, phi = np.meshgrid(ro, phi)
    Z = func(ro,phi)

    ax.contourf(phi, ro, np.real(Z), num=160, cmap=plt.cm.jet)
    # ax.plot(np.linspace(0, 2 * np.pi, 100), [1] * 100, c='k')
    ax.set_aspect('equal')
    plt.draw()

    plt.draw()

def get_real_roots(func, range_x=[0.5, 5], num=20):
    roots = set()

    for x in np.linspace(*range_x, num=num):
        root = False
        try:
            root = opt.newton(func=func,
                              x0=np.array([x + 0 * 1j]))
        except:
            pass

        if root:
            if min(range_x) < np.real(root[0]) < max(range_x):
                if all([np.abs(r - root) > 1.e-10 for r in roots]):
                    roots.add(root[0])
    return roots

def get_complex_roots(func, range_x=[0.5, 5], range_y=[-1, 1], num=20):
    roots = set()

    for x in np.linspace(*range_x, num=num):
        for y in np.linspace(*range_y, num=num):
            root = False
            try:
                root = opt.newton(func=func,
                                  x0=np.array([x + y * 1j]))
            except:
                pass

            if root:
                if min(range_x) < np.real(root[0]) < max(range_x):
                    if min(range_y) < np.imag(root[0]) < max(range_y):
                        if all([np.abs(r - root) > 1.e-10 for r in roots]):
                            roots.add(root[0])
    return roots

if __name__ == '__main__':
    bessel_function_ouput(TM=False)

    # print(get_real_roots(func=np.sin,range_x=[-1,10]))
    # print(get_complex_roots(func=np.sinh,range_x=[-1,1],range_y=[-1,11]))

    n, m, eps = 1, 1, 10
    fig = plt.figure()
    fig.canvas.set_window_title('Closed waveguide')
    ax = fig.gca(projection='polar')
    root = eigenvalues_TE(n=n, m=m, eps=eps, r=1)
    print(root)
    ax.set_title(f' Wave function orders {n} {m} for k={round(root,5)}')

    func = eigen_function_TE(n=n,
                             k=root,
                             eps=eps,
                             even=False)
    draw_contour(func, ax=ax)
    plt.show()
