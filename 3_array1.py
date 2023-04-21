import numpy as np
sample = np.array([[2, 4, 6, 8, 6], [23, 56, 45, 10, 83], [98, 12 ,34, 78, 78], [21, 63, 78, 84, 53]])
print(sample)

new_array = sample[::2, 1::2]
print(new_array)
