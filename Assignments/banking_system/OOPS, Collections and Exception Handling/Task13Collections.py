from collections import defaultdict
from datetime import datetime


class Customer:
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}, {self.phone}, {self.address}"


class Account:
    last_acc_no = 1000

    def __init__(self, account_type, balance, customer):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def __str__(self):
        return f"Acc No: {self.account_number}, Type: {self.account_type}, Balance: {self.balance}, Customer: [{self.customer}]"


class SavingsAccount(Account):
    def __init__(self, balance, customer, interest_rate=0.03):
        if balance < 500:
            print("Minimum balance of 500 required. Setting to 500.")
            balance = 500
        super().__init__("Savings", balance, customer)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


class CurrentAccount(Account):
    def __init__(self, balance, customer, overdraft_limit=1000):
        super().__init__("Current", balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return self.balance
        else:
            raise Exception("Overdraft limit exceeded")


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", 0, customer)


class HMBank:
    def __init__(self):
        self.accounts = []  # Change to set() or {} for Task 13 part 2 and 3

    def create_account(self, customer, acc_type, balance):
        if acc_type.lower() == "savings":
            acc = SavingsAccount(balance, customer)
        elif acc_type.lower() == "current":
            acc = CurrentAccount(balance, customer)
        elif acc_type.lower() == "zerobalance":
            acc = ZeroBalanceAccount(customer)
        else:
            print("Invalid account type")
            return None

        if isinstance(self.accounts, list):
            self.accounts.append(acc)
        elif isinstance(self.accounts, set):
            self.accounts.add(acc)
        elif isinstance(self.accounts, dict):
            self.accounts[acc.account_number] = acc

        print(f"Account Created: {acc.account_number}")

    def get_account(self, acc_no):
        if isinstance(self.accounts, list):
            for acc in self.accounts:
                if acc.account_number == acc_no:
                    return acc
        elif isinstance(self.accounts, set):
            for acc in self.accounts:
                if acc.account_number == acc_no:
                    return acc
        elif isinstance(self.accounts, dict):
            return self.accounts.get(acc_no)
        return None

    def list_accounts(self):
        if isinstance(self.accounts, list):
            sorted_accounts = sorted(self.accounts, key=lambda x: x.customer.first_name)
            for acc in sorted_accounts:
                print(acc)
        elif isinstance(self.accounts, set):
            sorted_accounts = sorted(self.accounts, key=lambda x: x.customer.first_name)
            for acc in sorted_accounts:
                print(acc)
        elif isinstance(self.accounts, dict):
            for acc in self.accounts.values():
                print(acc)

    def deposit(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            acc.balance += amount
            print(f"Deposited. New Balance: {acc.balance}")
        else:
            print("Account not found")

    def withdraw(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            try:
                if hasattr(acc, 'withdraw'):
                    acc.withdraw(amount)
                elif acc.balance >= amount:
                    acc.balance -= amount
                else:
                    raise Exception("Insufficient balance.")
                print(f"New Balance: {acc.balance}")
            except Exception as e:
                print(e)
        else:
            print("Account not found")


def main():
    bank = HMBank()
    while True:
        print("\n1.Create\n2.Deposit\n3.Withdraw\n4.List\n5.Calculate Interest\n6.Exit")
        ch = input("Choice: ")
        if ch == "1":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            acc_type = input("Account Type (Savings/Current/ZeroBalance): ")
            if acc_type.lower() == "zerobalance":
                balance = 0
            else:
                balance = float(input("Initial balance: "))
            cust = Customer(fname, lname, email, phone, address)
            bank.create_account(cust, acc_type, balance)
        elif ch == "2":
            acc = int(input("Account number: "))
            amt = float(input("Amount: "))
            bank.deposit(acc, amt)
        elif ch == "3":
            acc = int(input("Account number: "))
            amt = float(input("Amount: "))
            bank.withdraw(acc, amt)
        elif ch == "4":
            bank.list_accounts()
        elif ch == "5":
            acc = int(input("Account number: "))
            account = bank.get_account(acc)
            if isinstance(account, SavingsAccount):
                interest = account.calculate_interest()
                print(f"Interest {interest} added. New Balance: {account.balance}")
            else:
                print("Interest applies only to Savings Account.")
        elif ch == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
