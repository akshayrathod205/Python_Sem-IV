import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91, 32]
f = np.array(fvalues)
print("Values in Fahrenheit:")
print(f)
print("Values in Centigrade:")
print(np.round((5*f/9 - 5*32/9), 2))