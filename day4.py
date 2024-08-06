#Problem 1: Write a python program to plot matplotlib graph
import matplotlib.pyplot as plt
import numpy as np

np_x = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
np_y = np.array([21, 22, 23, 24, 28, 15, 29, 17, 12, 13, 11, 14, 18, 19, 20])

plt.scatter(np_x, np_y)
plt.show()

#Problem 2: Write a python program to slicing in an array
import numpy as np
np_2d = np.array([[2,3],[4,5]])
print(np_2d[-2,1])
