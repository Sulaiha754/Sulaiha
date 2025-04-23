from bank_account import BankAccount

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000.0
    def __init__(self, account_number="", customer_name="", balance=0.0):
        super().__init__(account_number, customer_name, balance)
    def deposit(self, amount: float):
        self.balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self.balance:.2f}")
    def withdraw(self, amount: float):
        if self.balance + CurrentAccount.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance:.2f}")
        else:
            print("Overdraft limit exceeded.")
    def calculate_interest(self):
        print("No interest for Current Account.")
