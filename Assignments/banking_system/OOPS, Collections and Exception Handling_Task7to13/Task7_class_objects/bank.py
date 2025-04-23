from customer import Customer
from account import Account

""" Create a Bank class to represent the banking system. Perform the following operation in
main method:
o create object for account class by calling parameter constructor.
o deposit(amount: float): Deposit the specified amount into the account.
o withdraw(amount: float): Withdraw the specified amount from the account.
o calculate_interest(): Calculate and add interest to the account balance for savings
accounts."""

from customer import Customer
from account import Account

class Bank:
    def main(self):
        # Create Customer
        customer = Customer(101, "Sulaiha", "bari", "sulai@example.com", "9876543210", "Chennai")
        customer.print_customer_info()
        print("")

        # Create Account
        account = Account(1001, "Savings", 5000.0)
        account.print_account_info()
        print("")

        # Deposit
        account.deposit(2000)
        account.print_account_info()
        print("")

        # Withdraw
        account.withdraw(1000)
        account.print_account_info()
        print("")

        # Calculate interest
        account.calculate_interest()
        account.print_account_info()

if __name__ == "__main__":
    bank = Bank()
    bank.main()