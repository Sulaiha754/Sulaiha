from savings_account import SavingsAccount
from current_account import CurrentAccount


def main():
    print("=== Welcome to the Bank System ===")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    choice = int(input("Enter your choice: "))
    acc_number = input("Enter account number: ")
    cust_name = input("Enter customer name: ")
    balance = float(input("Enter initial balance: "))
    if choice == 1:
        interest_rate = float(input("Enter interest rate (e.g., 0.03 for 3%): "))
        account = SavingsAccount(acc_number, cust_name, balance, interest_rate)
    elif choice == 2:
        account = CurrentAccount(acc_number, cust_name, balance)
    else:
        print("Invalid choice.")
        return
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Calculate Interest\n4. Print Info\n5. Exit")
        option = int(input("Enter option: "))
        if option == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif option == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif option == 3:
            account.calculate_interest()
        elif option == 4:
            account.print_info()
        elif option == 5:
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()