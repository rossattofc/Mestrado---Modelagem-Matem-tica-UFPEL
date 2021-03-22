import numpy as np

a = ([[3, 2, -1],
     [1, 3, 1],
     [2, 2, -2]])
b = ([0, 1, 2])

x = np.linalg.solve(a, b)
x
