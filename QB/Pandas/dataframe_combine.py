import pandas as pd
sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])
print("Original")
print(sr1)
print(sr2)

print("Combine data frames")
df = pd.DataFrame(sr1, sr2).reset_index()
print(df.head())

print("Using pandas, give specific name to column")
df = pd.DataFrame({'col1': sr1, 'col2': sr2})
print(df.head(5))