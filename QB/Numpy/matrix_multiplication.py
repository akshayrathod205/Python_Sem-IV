import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original:")
print(p)
print(q)

result = np.dot(p, q)
print(result)