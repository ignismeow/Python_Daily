#Problem 1: Write a python program to plot matplotlib graph
import matplotlib.pyplot as plt
import numpy as np

np_x = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
np_y = np.array([21, 22, 23, 24, 28, 15, 29, 17, 12, 13, 11, 14, 18, 19, 20])

plt.scatter(np_x, np_y)
plt.show()
