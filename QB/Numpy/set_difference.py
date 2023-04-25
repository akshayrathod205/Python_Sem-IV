import numpy as np
a = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ", a)
b = [10, 30, 40, 50, 70]
print("Array2: ", b)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(a, b))
