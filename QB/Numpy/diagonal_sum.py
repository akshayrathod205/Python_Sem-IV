import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array")
print(a)

result = np.trace(a)
print("Condition number of matrix:")
print(result)
