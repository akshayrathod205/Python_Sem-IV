import numpy as np

x = np.ones((3, 3))
print("Checboard pattern:")
x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print(x)