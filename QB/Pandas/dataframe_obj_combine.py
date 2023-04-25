import pandas as pd

df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})

result = df1.combine_first(df2)
result1 = df2.combine_first(df1)
print(result)
print(result1)