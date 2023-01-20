import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    fig = plt.figure()
    plt.title('population size: 50')
    # x = np.array([100, 100, 100, 100, 17, 100, 100, 100, 100, 100, 100, 100, 100, 8, 100, ])
    # y = np.array([2, 4, 4, 2, 0, 2, 4, 4, 2, 2, 2, 2, 2, 0, 3])

    plt.xlabel('Num of generations')
    plt.ylabel('Fitness')
    # plt.plot(x, y, color="red", linestyle="-.")
    # plt.legend(loc="upper left")
    plt.scatter(x,y)
    # plt.colorbar()
    plt.show()
