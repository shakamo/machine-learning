import numpy as np
from matplotlib import pyplot as plt


def show_2d(x, y, z, x_name, y_name):
    # 描画する
    np.where(0 < z)
    plt.scatter(x, y, c=z, vmin=min(z[np.where(0 < z)]), vmax=max(z[np.where(0 < z)]))

    plt.xlabel(x_name)
    plt.ylabel(y_name)

    plt.colorbar()
    plt.show()


def show_3d(a, b, c, y, a_name, b_name, c_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    np.where(0 < y)
    p = ax.scatter(a, b, c, c=y, vmin=min(y[np.where(0 < y)]), vmax=max(y[np.where(0 < y)]))

    ax.set_xlabel(a_name)
    ax.set_ylabel(b_name)
    ax.set_zlabel(c_name)

    fig.colorbar(p)
    plt.show()

    plt.savefig('viz.png')
