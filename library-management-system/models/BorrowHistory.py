from datetime import datetime,timedelta
from decimal import Decimal

class BorrowHistory:

    def __init__(self,borrow_id,user_id,book_id,borrow_date):

        self.borrow_id = borrow_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = None
        self.due_date = borrow_date + timedelta(days=14)
        self.fine_per_day = Decimal("1.50")

    def is_active(self):

        return self.return_date is None
    
    def calculate_overdue_fine(self):

        if self.return_date is not None:
            comparison_date = self.return_date

        else:
            comparison_date = datetime.now()

        if comparison_date <= self.due_date:

            return 0

        overdue_days = (comparison_date - self.due_date).days

        return overdue_days * self.fine_per_day



