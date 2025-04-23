"""Task 8: Inheritance and polymorphism

1. Overload the deposit and withdraw methods in Account class as mentioned below.
• deposit(amount: float): Deposit the specified amount into the account.
• withdraw(amount: float): Withdraw the specified amount from the account. withdraw
amount only if there is sufficient fund else display insufficient balance.
• deposit(amount: int): Deposit the specified amount into the account.
• withdraw(amount: int): Withdraw the specified amount from the account. withdraw
amount only if there is sufficient fund else display insufficient balance.
• deposit(amount: double): Deposit the specified amount into the account.
• withdraw(amount: double): Withdraw the specified amount from the account. withdraw
amount only if there is sufficient fund else display insufficient balance.

2. Create Subclasses for Specific Account Types
• Create subclasses for specific account types (e.g., `SavingsAccount`, `CurrentAccount`)
that inherit from the `Account` class.
o SavingsAccount: A savings account that includes an additional attribute for
interest rate. override the calculate_interest() from Account class method to
calculate interest based on the balance and interest rate.
o CurrentAccount: A current account that includes an additional attribute
overdraftLimit. A current account with no interest. Implement the withdraw()
method to allow overdraft up to a certain limit (configure a constant for the
overdraft limit).

3. Create a Bank class to represent the banking system. Perform the following operation in main
method:
• Display menu for user to create object for account class by calling parameter
constructor. Menu should display options `SavingsAccount` and `CurrentAccount`. user
can choose any one option to create account. use switch case for implementation.
• deposit(amount: float): Deposit the specified amount into the account.
• withdraw(amount: float): Withdraw the specified amount from the account. For saving
account withdraw amount only if there is sufficient fund else display insufficient balance.
For Current Account withdraw limit can exceed the available balance and should not
exceed the overdraft limit.
• calculate_interest(): Calculate and add interest to the account balance for savings
accounts."""

class Account:
    def __init__(self, account_number=None, account_type=None, balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += float(amount)
        print(f"Deposited: {amount}. Current Balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= float(amount):
            self.__balance -= float(amount)
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def calculate_interest(self):
        interest = self.__balance * 0.045
        print(f"Interest: {interest}")
        return interest

    def get_balance(self):
        return self.__balance

    def get_account_type(self):
        return self.__account_type

    def get_account_number(self):
        return self.__account_number

    def set_balance(self, balance):
        self.__balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=0.045):
        super().__init__(account_number, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Savings Account Interest: {interest}")
        self.set_balance(self.get_balance() + interest)
        return interest

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000.0

    def __init__(self, account_number, balance):
        super().__init__(account_number, "Current", balance)

    def withdraw(self, amount):
        if self.get_balance() + CurrentAccount.OVERDRAFT_LIMIT >= float(amount):
            self.set_balance(self.get_balance() - float(amount))
            print(f"Withdrawn: {amount}. New Balance: {self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit!")

def main():
    print("Welcome to HexaBank")
    print("Choose Account Type:")
    print("1. Savings Account")
    print("2. Current Account")
    choice = int(input("Enter choice: "))

    acc_number = input("Enter Account Number: ")
    balance = float(input("Enter Initial Balance: "))

    if choice == 1:
        account = SavingsAccount(acc_number, balance)
    elif choice == 2:
        account = CurrentAccount(acc_number, balance)
    else:
        print("Invalid choice.")
        return

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Calculate Interest\n4. Exit")
        option = int(input("Enter option: "))

        if option == 1:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        elif option == 2:
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        elif option == 3:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()
            else:
                print("Interest not applicable for Current Account.")
        elif option == 4:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
