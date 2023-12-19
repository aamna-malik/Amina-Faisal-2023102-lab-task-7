class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Library Books:")
            for book in self.books:
                print(book)

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print(f"No books found with the title '{title}'.")
        else:
            print(f"Books found with the title '{title}':")
            for book in found_books:
                print(book)


# Example usage:

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
book3 = Book("1984", "George Orwell", "978-0451524935")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
library.display_books()

# Search for a book by title
library.search_book_by_title("To Kill a Mockingbird")
library.search_book_by_title("Harry Potter")
