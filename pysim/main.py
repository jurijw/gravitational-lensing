import matplotlib.pyplot as plt
import numpy as np


def setup():
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    xv, yv = np.meshgrid(x, y)
    plt.imshow(alpha(xv, yv))
    plt.show()


def alpha(x, y):
    return x + y


def main():
    setup()


if __name__ == '__main__':
    main()
