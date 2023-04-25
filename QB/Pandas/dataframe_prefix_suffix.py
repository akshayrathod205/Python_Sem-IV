import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66], 'X':[78,85,96,80,86], 'Y':[84,94,89,83,86], 'Z':[86,97,96,72,83]})
print(df)

print("Add prefix")
print(df.add_prefix("OO_"))

print("Add suffix")
print(df.add_suffix("_OO"))