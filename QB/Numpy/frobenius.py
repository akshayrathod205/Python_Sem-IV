import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array")
print(a)

print("Frobenius norm and condition number:")
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))