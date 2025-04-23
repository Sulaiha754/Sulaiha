
"""Task 2: Nested Conditional Statements
Create a program that simulates an ATM transaction. Display options such as "Check Balance,"
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate
messages for success or failure"""

balance = float(input("Enter your current balance: "))
while True:  
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
        print(f"Your current balance is ₹{balance:.2f}")
    elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= balance:
            if withdraw_amount % 100 == 0 or withdraw_amount % 500 == 0:
                balance -= withdraw_amount
                print(f"Withdrawal successful. New balance: ₹{balance:.2f}")
            else:
                print("Withdrawal amount must be in multiples of 100 or 500.")
        else:
            print("Insufficient balance for this withdrawal.")
    elif choice == 3:
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"Deposit successful. New balance: ₹{balance:.2f}")

    elif choice == 4:
        print("Exiting ATM.")
        break  
    else:
        print("Invalid choice")