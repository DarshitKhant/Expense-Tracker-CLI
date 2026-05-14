from datetime import datetime
class Expense:
    def __init__(self,id, amount, category, note, date=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.note = note
        # give current date if date is not given my user.
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
