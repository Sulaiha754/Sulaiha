"""task 9: Abstraction

1. Create an abstract class BankAccount that represents a generic bank account. It should include
the following attributes and methods:

o Account number.
o Customer name.
o Balance.
• Constructors:
 Implement default constructors and overload the constructor with Account
attributes, generate getter and setter, print all information of attribute methods
for the attributes.

• Abstract methods:
o deposit(amount: float): Deposit the specified amount into the account.
o withdraw(amount: float): Withdraw the specified amount from the account
(implement error handling for insufficient funds).

 calculate_interest(): Abstract method for calculating interest.

2. Create two concrete classes that inherit from BankAccount:
• SavingsAccount: A savings account that includes an additional attribute for interest rate.
Implement the calculate_interest() method to calculate interest based on the balance
and interest rate.

• CurrentAccount: A current account with no interest. Implement the withdraw() method
to allow overdraft up to a certain limit (configure a constant for the overdraft limit).

3. Create a Bank class to represent the banking system. Perform the following operation in main
method:
• Display menu for user to create object for account class by calling parameter
constructor. Menu should display options `SavingsAccount` and `CurrentAccount`. user
can choose any one option to create account. use switch case for implementation.

create_account should display sub menu to choose type of accounts.
o Hint: Account acc = new SavingsAccount(); or Account acc = new
CurrentAccount();
• deposit(amount: float): Deposit the specified amount into the account.
• withdraw(amount: float): Withdraw the specified amount from the account. For saving
account withdraw amount only if there is sufficient fund else display insufficient balance.

For Current Account withdraw limit can exceed the available balance and should not
exceed the overdraft limit.

• calculate_interest(): Calculate and add interest to the account balance for savings
accounts."""

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number="", customer_name="", balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, number):
        self.account_number = number

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, name):
        self.customer_name = name

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ₹{self.balance:.2f}")
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
