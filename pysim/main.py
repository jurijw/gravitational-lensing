import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng


def setup():
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    xv, yv = np.meshgrid(x, y)
    # plt.imshow(alpha(xv, yv))
    # plt.show()

    rng = default_rng()
    X, Y = rng.standard_normal((10, 10))
    plt.scatter(X, Y)
    plt.show()


def alpha(x, y):
    return x + y


def main():
    setup()


if __name__ == '__main__':
    main()
