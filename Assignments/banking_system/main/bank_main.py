import sys
sys.path.append('C:/Users/User/Desktop/hexaware/Assignment/HMBank/banking_system')

from dao.bank_impl import BankServiceImpl
from entity.customer import Customer

bank = BankServiceImpl()

while True:
    print("\n--- HMBank  Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Get Balance")
    print("5. Get Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            fname = input("First Name: ")
            lname = input("Last Name: ")
            dob = input("DOB (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            acc_type = input("Account Type (savings/current): ")
            balance = float(input("Initial Balance: "))
            customer = Customer(0, fname, lname, dob, email, phone, address)
            bank.create_account(customer, acc_type, balance)

        elif choice == '2':
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter Deposit Amount: "))
            bank.deposit(acc_id, amount)

        elif choice == '3':
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter Withdrawal Amount: "))
            bank.withdraw(acc_id, amount)

        elif choice == '4':
            acc_id = int(input("Enter Account ID: "))
            print(f"Current Balance: ₹{bank.get_balance(acc_id)}")

        elif choice == '5':
            acc_id = int(input("Enter Account ID: "))
            details = bank.get_account_details(acc_id)
            print(f"Customer Name: {details.first_name} {details.last_name}")
            print(f"Account Type: {details.account_type}")
            print(f"Balance: ₹{details.balance}")

        elif choice == '6':
            print("Exiting Banking System. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

    except Exception as e:
        print(f"Error: {e}")
