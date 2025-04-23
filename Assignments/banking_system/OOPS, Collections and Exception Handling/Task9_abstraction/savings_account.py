from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number="", customer_name="", balance=0.0, interest_rate=0.03):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate
    def deposit(self, amount: float):
        self.balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self.balance:.2f}")
    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance:.2f}")
        else:
            print("Insufficient balance.")
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}")
