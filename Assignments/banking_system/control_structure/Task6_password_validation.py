
"""Task 6: Password Validation
Create a program that maintains a list of bank transactions (deposits and withdrawals) for a customer.
Use a while loop to allow the user to keep adding transactions until they choose to exit. Display the
transaction history upon exit using looping statements"""

# Set password
correct_password = "bank123"

# Password validation
entered_password = input("Enter your password to access your bank account: ")
if entered_password != correct_password:
    print("Incorrect password. Access denied.")
else:
    print("Access granted. Welcome!")

    transactions = []  # List to store transactions
    balance = 0        # Initial balance
    while True:
        print("\nChoose a transaction:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("Insufficient balance.")
                transactions.append(f"Failed withdrawal attempt of ₹{amount}")
            else:
                balance -= amount
                transactions.append(f"Withdrew ₹{amount}")
                print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")
        elif choice == '3':
            print("\nExiting! Here is your transaction history:")
            for index, t in enumerate(transactions, start=1):
                print(f"{index}. {t}")
            print(f"\nFinal Balance: ₹{balance}")
            break
        else:
            print("Invalid choice.")
