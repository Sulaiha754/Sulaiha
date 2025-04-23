
"""Task 3: Loop Structures
You are responsible for calculating compound interest on savings accounts for bank customers. You
need to calculate the future balance for each customer's savings account after a certain number of years.
Tasks:
1. Create a program that calculates the future balance of a savings account.
2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers.
3. Prompt the user to enter the initial balance, annual interest rate, and the number of years.
4. Calculate the future balance using the formula:
future_balance = initial_balance * (1 + annual_interest_rate/100)^years.
5. Display the future balance for each customer"""

num_customers = int(input("Enter the number of customers: "))
for i in range(num_customers):
    print(f"\nCustomer {i+1}")
    initial_balance = float(input("Enter initial balance: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter number of years: "))
    future_balance = initial_balance * (1 + annual_rate / 100) ** years
    print(f"Future Balance after {years} years: ₹{future_balance:.2f}")
