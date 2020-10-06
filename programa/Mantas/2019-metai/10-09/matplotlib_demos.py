import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

points = np.array([[-1, 15, 2], [2, 6, 8], [5, 4, 20], [1, 5, 20], [3, 9, 12]])
ax = plt.axes(projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='blue')
plt.show()