class Expense:
    def __init__(self, expense_id, user_id, category_id, amount, date, description):
        self.expense_id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"Expense(ID: {self.expense_id}, User: {self.user_id}, Category: {self.category_id}, Amount: {self.amount}, Date: {self.date}, Description: {self.description})"
