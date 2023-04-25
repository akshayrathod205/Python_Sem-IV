import numpy as np

x = np.arange(12, 38)
print("Original array:")
print(x)

print("Reverse array:")
x = x[ : : -1]
print(x)