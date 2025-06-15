class Book:
    """A class representing a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""
    
    def __init__(self):
        """Initialize an empty library with a list of books."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
    
    def return_book(self, title):
        """Return a book by title if it exists."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
    
    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")