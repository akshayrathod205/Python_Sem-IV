import numpy as np

print("Creating a 8X3 matrix")
sample = np.arange(10, 34, 1)
sample = sample.reshape(8 ,3)
print(sample)

print("Dividing the array into 4 sub arrays")
subArray = np.split(sample, 4)
print(subArray)
