import matplotlib.pyplot as plt
import numpy as np

# Generate random data points
np.random.seed(123)  # For reproducibility
data = np.random.randint(0, 100, 1000)

# Define histogram bins
bins = np.arange(0, 101, 5)  # Bin edges from 0 to 100 with step of 5

# Plotting the histogram
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins=bins, edgecolor='black')

# Adding labels and title
ax.set_xlabel('Range')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Randomly Generated Data\nwith Ranges [0-5, 5-10, 10-15, ... 95-100]')

plt.show()
