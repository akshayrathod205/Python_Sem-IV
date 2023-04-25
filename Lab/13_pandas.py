import pandas as pd

data = {
    'ISBN': ['978-0451524935', '978-0141439617', '978-0486275482', '978-0486404528', '978-0486424786', '978-0486292748', '978-0486280554', '978-0486424564', '978-0486280530', '978-0486280974'],
    'Title': ['Pride and Prejudice', 'Wuthering Heights', 'The Adventures of Tom Sawyer', 'The Importance of Being Earnest', 'The Picture of Dorian Gray', 'The War of the Worlds', 'The Time Machine', 'The Hound of the Baskervilles', 'The Invisible Man', 'Frankenstein'],
    'Author': ['Jane Austen', 'Emily Bronte', 'Mark Twain', 'Oscar Wilde', 'Oscar Wilde', 'H.G. Wells', 'H.G. Wells', 'Arthur Conan Doyle', 'H.G. Wells', 'Mary Shelley'],
    'Publication': ['Penguin Classics', 'Penguin Classics', 'Dover Publications', 'Dover Publications', 'Dover Publications', 'Dover Publications', 'Dover Publications', 'Dover Publications', 'Dover Publications', 'Dover Publications'],
    'Year Published': [1813, 1847, 1876, 1895, 1890, 1898, 1895, 1902, 1897, 1818],
    'Price': [10.99, 9.99, 4.00, 3.00, 4.00, 5.00, 5.00, 4.00, 4.00, 5.00],
    'Copies sold of first edition': [5000, 4000, 6000, 3000, 2000, 8000, 7000, 4000, 6000, 4000],
    'Copies sold in second edition': [3000, 2000, 4000, 2000, 1000, 5000, 4000, 3000, 4000, 2000],
    'Copies sold in third edition': [2000, 1000, 2000, 1000, 500, 3000, 2000, 1000, 2000, 1000]
}

df = pd.DataFrame(data)

# Display the number of rows and columns in dataframe
print("Number of rows and columns:", df.shape)

# Give the descriptive statistics of the created dataset.
print("Descriptive statistics:\n", df.describe())

# Display distinct publication names for the dataset.
print("Distinct publication names:\n", df['Publication'].unique())

# Display the book title and author names published by “Metro Publication”
print("Books published by Metro Publication:\n", df.loc[df['Publication'] == 'Metro Publication', ['Title', 'Author']])

# Rename columns “Copies sold in first edition”, “Copies sold in second edition” and “Copies sold in third edition” to FE, SE and TE respectively
df = df.rename(columns={'Copies sold of first edition': 'FE', 'Copies sold in second edition': 'SE', 'Copies sold in third edition': 'TE'})

# To add a column “Average sale” to the dataframe derived as (average of FE, SE and TE) * Price:
df['Average sale'] = ((df['FE'] + df['SE'] + df['TE']) / 3) * df['Price']

# 7. Display the details of books grouped by author
grouped_books = df.groupby('Author')
print(grouped_books.apply(lambda x: x[['Title', 'Publication', 'Year Published', 'Price']]))

# 8. For each group obtained in above query display maximum value of Average sale
print(grouped_books['Price'].max())

# Removing duplicates from index
# df = df.reset_index().drop_duplicates(subset=['Author', 'Publication']).set_index('Author')
df = df.drop_duplicates(subset=['Author', 'Publication'])

# Reshaping the dataframe
reshaped_books = df.pivot(index='Author', columns='Publication', values='Title')
print(reshaped_books)
