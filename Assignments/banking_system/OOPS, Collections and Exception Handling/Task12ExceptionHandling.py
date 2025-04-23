class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)


class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number"):
        self.message = message
        super().__init__(self.message)


class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded"):
        self.message = message
        super().__init__(self.message)


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
            raise OverDraftLimitExceededException("Overdraft limit exceeded")


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", 0, customer)


class BankService:
    def __init__(self):
        self.accounts = []

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
        self.accounts.append(acc)
        print(f"Account Created: {acc.account_number}")

    def get_account(self, acc_no):
        for acc in self.accounts:
            if acc.account_number == acc_no:
                return acc
        return None

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
                    raise InsufficientFundException("Insufficient balance.")
                print(f"New Balance: {acc.balance}")
            except Exception as e:
                print(e)
        else:
            print("Account not found")

    def get_balance(self, acc_no):
        acc = self.get_account(acc_no)
        if acc:
            print(f"Current Balance: {acc.balance}")
        else:
            print("Account not found")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print("Transfer successful")
            else:
                raise InsufficientFundException("Insufficient funds for transfer")
        else:
            raise InvalidAccountException("Invalid account number(s)")

    def get_account_details(self, acc_no):
        acc = self.get_account(acc_no)
        if acc:
            print(acc)
        else:
            print("Account not found")

    def list_accounts(self):
        for acc in self.accounts:
            print(acc)

    def calculate_interest(self):
        try:
            acc_no = int(input("Enter account number to calculate interest: "))
            account = self.get_account(acc_no)
            if account and isinstance(account, SavingsAccount):
                new_balance = account.calculate_interest()
                print(f"Interest added. New balance: {new_balance}")
            else:
                print("Interest calculation is only available for Savings Accounts.")
        except Exception as e:
            print(f"Error calculating interest: {e}")


def main():
    bank = BankService()
    while True:
        try:
            print("\n1.Create\n2.Deposit\n3.Withdraw\n4.Balance\n5.Transfer\n6.Details\n7.List\n8.Interest\n9.Exit")
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
                acc = int(input("Account number: "))
                bank.get_balance(acc)
            elif ch == "5":
                f = int(input("From Acc: "))
                t = int(input("To Acc: "))
                amt = float(input("Amount: "))
                bank.transfer(f, t, amt)
            elif ch == "6":
                acc = int(input("Account number: "))
                bank.get_account_details(acc)
            elif ch == "7":
                bank.list_accounts()
            elif ch == "8":
                bank.calculate_interest()
            elif ch == "9":
                break
            else:
                print("Invalid option")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
