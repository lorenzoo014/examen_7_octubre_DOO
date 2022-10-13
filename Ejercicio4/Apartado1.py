
import matplotlib.pyplot as plt
import numpy as np
def graficaPuntosRojos():
    x = np.linspace(0, 10, 100)
    y = x**3

    plt.plot(x, y, 'ro')
    plt.show()

graficaPuntosRojos()


