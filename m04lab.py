#jose solis
#02/11/24
#m04LAB
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to store books
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Using next() to find the first book matching the given ID
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book) if book else jsonify({'message': 'Book not found'}), 404

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    # Creating a new book object and appending it to the list of books
    new_book = {"id": len(books) + 1, "book_name": data['book_name'], "author": data['author'], "publisher": data['publisher']}
    books.append(new_book)
    return jsonify(new_book), 201

# Route to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Using next() to find the first book matching the given ID
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.json
        # Updating the book with the new data
        book.update(data)
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Using next() to find the first book matching the given ID
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
