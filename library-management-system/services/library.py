from models.book import Book
from models.user import User

"""
Service layer for managing library operations.

Responsible for:
- Managing book and user entities
- Performing CRUD operations
- Handling borrowing and returning logic

"""


class Library:

    def __init__(self):

        self.books =  {}
        self.users = {}

    # --- BOOK OPERATIONS --- #

    def add_book(self,book):

        if book.book_id in self.books:
            raise ValueError("Book ID already exists.")

        self.books[book.book_id] = book

    def find_book(self,book_id):

        return self.books.get(book_id)

    # --- USER OPERATIONS --- #

    def add_user(self,user):
        
        if user.user_id in self.users:
            raise ValueError("User ID already exists.")
    
    def find_user(self,user_id):

        return self.users.get(user_id)