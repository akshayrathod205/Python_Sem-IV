import numpy as np
a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float64)
print("Original array:")
print(a)

U, s, V = np.linalg.svd(a, full_matrices=False)
q, r = np.linalg.qr(a)
print("Factor of array by Singular Value Decompostion")
print("U =\n", U, "s = \n", s, "V = \n", V)