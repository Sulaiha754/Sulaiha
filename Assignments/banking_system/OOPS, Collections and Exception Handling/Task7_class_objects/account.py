"""Create an `Account` class with the following confidential attributes:
 Account Number
 Account Type (e.g., Savings, Current)
 Account Balance
• Constructor and Methods
Implement default constructors and overload the constructor with Account
attributes,
 Generate getter and setter, (print all information of attribute) methods for the
attributes.
 Add methods to the `Account` class to allow deposits and withdrawals.
- deposit(amount: float): Deposit the specified amount into the account.
- withdraw(amount: float): Withdraw the specified amount from the account.
withdraw amount only if there is sufficient fund else display insufficient
balance.
- calculate_interest(): method for calculating interest amount for the available
balance. interest rate is fixed to 4.5%
"""

class Account:
    def __init__(self, account_number=None, account_type="", balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    # Setters
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Balance: ₹{self.__balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def calculate_interest(self):
        if self.__account_type.lower() == "savings":
            interest = self.__balance * 0.045
            self.__balance += interest
            print(f"Interest of ₹{interest:.2f} added to your balance.")
        else:
            print("Interest applicable only to savings account.")

