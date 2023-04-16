import os

filename = 'bookdata.txt'

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        print(f"{filename} does not exist. An empty file has been created.")
        num_books = 0
        while num_books < 3:
            book = {}
            book['title'] = input("Enter book title: ")
            book['author'] = input("Enter book author: ")
            book['type'] = input("Enter book type: ")
            book['publication'] = input("Enter book publication: ")
            book['price'] = input("Enter book price: ")
            f.write(str(book) + '\n')
            num_books += 1

with open(filename, 'r') as f:
    book_list = []
    for line in f:
        book = eval(line.strip())
        book_list.append(book)
    print("Book Details:")
    for book in book_list:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Type: {book['type']}")
        print(f"Publication: {book['publication']}")
        print(f"Price: {book['price']}")
