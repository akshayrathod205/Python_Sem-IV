import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original")
print(df)

print("Value of Row 1")
print(df.iloc[0])

print("Value of Row 4")
print(df.iloc[3])