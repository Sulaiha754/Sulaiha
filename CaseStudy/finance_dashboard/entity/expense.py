class Expense:
    def __init__(self, expense_id, user_id, category_id, amount, date, description):
        self.expense_id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.description = description
