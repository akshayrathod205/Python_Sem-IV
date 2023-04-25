import pandas as pd
import numpy as np

sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
df = pd.DataFrame(sdata)
df.index = pd.date_range('2023-01-04', periods=6)

print("Original")
print(df)

print("After interpolate")
print(df.interpolate())