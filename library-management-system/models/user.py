class User:

    def __init__(self,user_id,first_name,last_name,borrowed_books = None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []