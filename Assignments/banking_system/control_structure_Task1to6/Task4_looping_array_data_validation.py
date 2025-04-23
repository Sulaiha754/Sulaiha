
"""Task 4: Looping, Array and Data Validation
You are tasked with creating a program that allows bank customers to check their account balances.
The program should handle multiple customer accounts, and the customer should be able to enter their
account number, balance to check the balance.
Tasks:
1. Create a Python program that simulates a bank with multiple customer accounts.
2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and
balance until they enter a valid account number.
3. Validate the account number entered by the user.
4. If the account number is valid, display the account balance. If not, ask the user to try again."""
accounts = {
    1001: 15000.00,
    1002: 25450.75,
    1003: 8800.60,
    1004: 120000.00,
    1005: 500.00
}
while True:
    try:
        account_number = int(input("Enter your account number to check balance: "))
        if account_number in accounts:
            print(f"Account Number: {account_number}")
            print(f"Your balance is: ₹{accounts[account_number]:.2f}")
            break
        else:
            print("Invalid account number. Please try again.\n")
    except ValueError:
        print("Please enter a valid numeric account number.\n")
