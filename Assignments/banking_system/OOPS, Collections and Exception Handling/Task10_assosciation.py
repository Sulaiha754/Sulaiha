"""Task 10: Has A Relation / Association
1. Create a `Customer` class with the following attributes:
• Customer ID
• First Name
• Last Name
• Email Address (validate with valid email address)
• Phone Number (Validate 10-digit phone number)
• Address
• Methods and Constructor:
o Implement default constructors and overload the constructor with Account
attributes, generate getter, setter, print all information of attribute) methods for
the attributes.

2. Create an `Account` class with the following attributes:
• Account Number (a unique identifier).
• Account Type (e.g., Savings, Current)
• Account Balance
• Customer (the customer who owns the account)
• Methods and Constructor:
o Implement default constructors and overload the constructor with Account
attributes, generate getter, setter, (print all information of attribute) methods for
the attributes.

3. Create a Bank Class and must have following requirements:
1. Create a Bank class to represent the banking system. It should have the following methods:
• create_account(Customer customer, long accNo, String accType, float balance): Create
a new bank account for the given customer with the initial balance.
• get_account_balance(account_number: long): Retrieve the balance of an account given
its account number. should return the current balance of account.
• deposit(account_number: long, amount: float): Deposit the specified amount into the
account. Should return the current balance of account.
• withdraw(account_number: long, amount: float): Withdraw the specified amount from
the account. Should return the current balance of account.
• transfer(from_account_number: long, to_account_number: int, amount: float):
Transfer money from one account to another.
• getAccountDetails(account_number: long): Should return the account and customer
details.

2. Ensure that account numbers are automatically generated when an account is created, starting
from 1001 and incrementing for each new account.

3. Create a BankApp class with a main method to simulate the banking system. Allow the user to
interact with the system by entering commands such as "create_account", "deposit",
"withdraw", "get_balance", "transfer", "getAccountDetails" and "exit." create_account should
display sub menu to choose type of accounts and repeat this operation until user exit."""


class Customer:
    def __init__(self, customer_id="", first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.set_email(email)
        self.set_phone(phone)
        self.address = address

    def set_email(self, email):
        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            self.email = email
        else:
            raise ValueError("Invalid email format.")

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.phone = phone
        else:
            raise ValueError("Phone number must be 10 digits.")

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"


class Account:
    _account_number_counter = 1001

    def __init__(self, acc_type="Savings", balance=0.0, customer=None):
        self.account_number = Account._account_number_counter
        Account._account_number_counter += 1
        self.account_type = acc_type
        self.account_balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient balance!")
        return self.account_balance

    def __str__(self):
        return f"Account No: {self.account_number}\nAccount Type: {self.account_type}\nBalance: {self.account_balance:.2f}\n---Customer Info---\n{self.customer}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, acc_type, balance):
        account = Account(acc_type, balance, customer)
        self.accounts[account.account_number] = account
        print(f"Account created successfully! Account Number: {account.account_number}")

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.account_balance
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_acc = self.accounts.get(from_account_number)
        to_acc = self.accounts.get(to_account_number)
        if from_acc and to_acc:
            if from_acc.account_balance >= amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Invalid account number(s).")

    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")


class BankApp:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        while True:
            print("\n===== BANK MENU =====")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid option. Please try again.")

    def create_account(self):
        try:
            cid = input("Enter Customer ID: ")
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone (10-digit): ")
            address = input("Enter Address: ")

            customer = Customer(cid, fname, lname, email, phone, address)

            print("Select Account Type:")
            print("1. Savings")
            print("2. Current")
            acc_type = input("Enter choice: ")
            acc_type_str = "Savings" if acc_type == "1" else "Current"

            balance = float(input("Enter initial deposit amount: "))
            self.bank.create_account(customer, acc_type_str, balance)
        except ValueError as e:
            print(e)

    def deposit(self):
        try:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            new_balance = self.bank.deposit(acc_no, amount)
            if new_balance is not None:
                print(f"Deposit successful. New balance: {new_balance:.2f}")
        except ValueError:
            print("Invalid input.")

    def withdraw(self):
        try:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            new_balance = self.bank.withdraw(acc_no, amount)
            if new_balance is not None:
                print(f"Withdrawal successful. New balance: {new_balance:.2f}")
        except ValueError:
            print("Invalid input.")

    def get_balance(self):
        try:
            acc_no = int(input("Enter account number: "))
            balance = self.bank.get_account_balance(acc_no)
            if balance is not None:
                print(f"Current balance: {balance:.2f}")
        except ValueError:
            print("Invalid input.")

    def transfer(self):
        try:
            from_acc = int(input("Enter sender account number: "))
            to_acc = int(input("Enter receiver account number: "))
            amount = float(input("Enter amount to transfer: "))
            self.bank.transfer(from_acc, to_acc, amount)
        except ValueError:
            print("Invalid input.")

    def get_account_details(self):
        try:
            acc_no = int(input("Enter account number: "))
            self.bank.get_account_details(acc_no)
        except ValueError:
            print("Invalid input.")


# Run the banking app
if __name__ == "__main__":
    app = BankApp()
    app.run()
