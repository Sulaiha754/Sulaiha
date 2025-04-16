
class Transaction:
    def __init__(self, transaction_id, account_id, transaction_type, amount, transaction_date):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_date = transaction_date
