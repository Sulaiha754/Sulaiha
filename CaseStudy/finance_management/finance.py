
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from entity.income import Income
from entity.expense import Expense
from entity.user import User
from dao.financerepoimpl import FinanceRepoImpl

repo = FinanceRepoImpl()

def menu():
    print("""
====== Finance Manager Menu ======
1. Add User
2. View Users
3. Add Income
4. View Income
5. Edit Income
6. Delete Income
7. Add Expense
8. View Expense
9. Edit Expense
10. Delete Expense
11. View Income Categories
12. Add Income Category
13. View Expense Categories
14. Add Expense Category
15. Generate Income Report
16. Generate Expense Report
17. Exit
""")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            repo.add_user(username, password, email)

        elif choice == '2':
            users = repo.get_all_users()
            for u in users:
                print(u)

        elif choice == '3':
            user_id = int(input("User ID: "))
            category_name = input("Enter income category name: ")
            category_id = repo.get_income_category_id_by_name(category_name)
            if not category_id:
                print("Category not found. Please add it first.")
                continue
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")
            repo.add_income(user_id, category_id, amount, date, description)

        elif choice == '4':
            user_id = int(input("User ID: "))
            for row in repo.get_all_income(user_id):
                print(f"Income ID: {row[0]}, User ID: {row[1]}, Category: {row[2]}, Amount: {float(row[3])}, Date: {row[4]}, Description: {row[5]}")

        elif choice == '5':
            user_id = int(input("User ID: "))
            incomes = repo.get_all_income(user_id)
            if not incomes:
                print("No income records found.")
                continue

            print("\nYour Income Records:")
            print("ID\tCategory\tAmount\tDate\t\tDescription")
            for income in incomes:
                print(f"{income[0]}\t{income[2]}\t{income[3]}\t{income[4]}\t{income[5]}")

            income_id = int(input("Enter the Income ID to edit: "))

            print("\nAvailable Categories:")
            for cat in repo.get_income_categories():
                print(f"{cat[0]} - {cat[1]}")

            category_id = int(input("New Category ID: "))
            amount = float(input("New Amount: "))
            date = input("New Date (YYYY-MM-DD): ")
            description = input("New Description: ")
            repo.update_income(income_id, category_id, amount, date, description)
            print("✅ Income updated successfully.")

        elif choice == '6':
            income_id = int(input("Income ID to delete: "))
            repo.delete_income(income_id)

        elif choice == '7':
            user_id = int(input("User ID: "))
            category_name = input("Enter expense category name: ")
            category_id = repo.get_expense_category_id_by_name(category_name)
            if not category_id:
                print("Category not found. Please add it first.")
                continue
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")
            repo.add_expense(user_id, category_id, amount, date, description)

        elif choice == '8':
            user_id = int(input("User ID: "))
            for row in repo.get_all_expense(user_id):
                print(f"Expense ID: {row[0]}, User ID: {row[1]}, Category: {row[2]}, Amount: {float(row[3])}, Date: {row[4]}, Description: {row[5]}")

        elif choice == '9':
            user_id = int(input("User ID: "))
            expenses = repo.get_all_expense(user_id)
            if not expenses:
                print("No expense records found.")
                continue

            print("\nYour Expense Records:")
            print("ID\tCategory\tAmount\tDate\t\tDescription")
            for expense in expenses:
                print(f"{expense[0]}\t{expense[2]}\t{expense[3]}\t{expense[4]}\t{expense[5]}")

            expense_id = int(input("Enter the Expense ID to edit: "))

            print("\nAvailable Categories:")
            for cat in repo.get_expense_categories():
                print(f"{cat[0]} - {cat[1]}")

            category_id = int(input("New Category ID: "))
            amount = float(input("New Amount: "))
            date = input("New Date (YYYY-MM-DD): ")
            description = input("New Description: ")
            repo.update_expense(expense_id, category_id, amount, date, description)
            print("✅ Expense updated successfully.")

        elif choice == '10':
            expense_id = int(input("Expense ID to delete: "))
            repo.delete_expense(expense_id)

        elif choice == '11':
            for row in repo.get_income_categories():
                print(f"Category ID: {row[0]}, Category Name: {row[1]}")

        elif choice == '12':
            cat = input("New income category name: ")
            repo.add_income_category(cat)

        elif choice == '13':
            for row in repo.get_expense_categories():
                print(f"Category ID: {row[0]}, Category Name: {row[1]}")

        elif choice == '14':
            cat = input("New expense category name: ")
            repo.add_expense_category(cat)

        elif choice == '15':
            user_id = int(input("User ID: "))
            print("Total Income:", repo.get_income_report(user_id))

        elif choice == '16':
            user_id = int(input("User ID: "))
            print("Total Expense:", repo.get_expense_report(user_id))

        elif choice == '17':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
