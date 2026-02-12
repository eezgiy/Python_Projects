class BorrowHistory:

    def __init__(self,borrow_id,user_id,book_id,borrow_date):

        self.borrow_id = borrow_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = None