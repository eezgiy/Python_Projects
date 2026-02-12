class Book:

    def __init__(self,book_id,book_title,author,year,total_copies):
        self.book_id = book_id
        self.book_title = book_title
        self.author = author
        self.year = year
        self.total_copies = total_copies
        self.available_copies = total_copies

