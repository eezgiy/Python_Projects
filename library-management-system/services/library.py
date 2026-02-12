from models.Book import Book
from models.User import User
from models.BorrowHistory import BorrowHistory
from datetime import datetime

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
        self.borrowRecords = {}
        self.next_borrow_id = 1

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
        
        self.users[user.user_id] = user
    
    def find_user(self,user_id):

        return self.users.get(user_id)
    
    # --- BORROWHISTORY OPERATIONS --- #

    def find_borrow_history(self,borrow_id):

        return self.borrowRecords.get(borrow_id)
    
    # --- TRANSACTION MANAGEMENT --- #

    def borrow_book(self,user_id,book_id):

        user = self.find_user(user_id)

        if not user:

            raise ValueError("The user can not be found")
        
        book = self.find_book(book_id)

        if not book:
                
            raise ValueError("The book can not be found")
            
        if book.available_copies <= 0:
                
                raise ValueError("No available copies left")

        

        book.available_copies -= 1

        borrow_id = self.next_borrow_id
        self.next_borrow_id += 1

        borrow_date = datetime.now()

        borrow_history = BorrowHistory(borrow_id,user_id,book_id,borrow_date)

        self.borrowRecords[borrow_id] = borrow_history

        return borrow_history


    def return_book(self,borrow_id):

        borrow_record = self.find_borrow_history(borrow_id)

        if not borrow_record:
            raise ValueError("Borrow record not found")
        
        if borrow_record.return_date is not None:
            raise ValueError("Book already returned")
        
        borrow_record.return_date = datetime.now()

        book = self.find_book(borrow_record.book_id)
        book.available_copies += 1

        return borrow_record

