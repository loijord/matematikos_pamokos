import matplotlib.pyplot as plt
import numpy as np


def grafikas(sharpness=6):
    fill = np.linspace(0, 1, sharpness)
    line1, = plt.plot(fill, np.sin(2 * np.pi * fill), color='blue')
    line2, = plt.plot(fill, 0.5 * np.sin(2 * np.pi * fill) + 0.5 * np.sin(2 * np.pi * fill) ** 2, color='green')
    line3, = plt.plot(fill, np.sin(2 * np.pi * fill) ** 2, color='yellow')
    plt.legend((line1, line2, line3), ('pure sine', 'hybrid', 'square sine'))
    plt.show()


grafikas(100)