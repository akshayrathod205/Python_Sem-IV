import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print("Original")
print(a)
print(b)

result = np.einsum("n, n", a, b)
print("Einstein Summation: ",result)

x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print("Original Higher Dimension: ")
print(x)
print(y)

result1 = np.einsum("mk, kn", x, y)
print("Einstein Summation: ")
print(result1)