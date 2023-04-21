from flask import Flask, render_template, redirect, jsonify, request

app = Flask(__name__)

# Data for books in the library (dummy data)
books = [
    {"number": 1, "title": "Book 1", "author": "Author 1", "publication": "Publication 1", "isbn": "123456789"},
    {"number": 2, "title": "Book 2", "author": "Author 2", "publication": "Publication 2", "isbn": "987654321"},
    {"number": 3, "title": "Book 3", "author": "Author 3", "publication": "Publication 3", "isbn": "456789123"}
]

@app.route('/')
def home():
    return "Welcome to the Library!"

@app.route('/books', methods=['GET'])
def view_books():
    return render_template('books.html', books=books)

@app.route('/books/search', methods=['GET'])
def search_books():
    isbn = request.args.get('isbn')
    book = None
    for b in books:
        if b['isbn'] == isbn:
            book = b
            break
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"})

if __name__ == '__main__':
    app.run(debug=True)
