from util.dbconnutil import DBConnUtil
from entity.expense import Expense
from entity.income import Income
from exception.expensenotfoundexception import ExpenseNotFoundException
from exception.invaliduserexception import InvalidUserException

class FinanceRepoImpl:

    def register_user(self, username, email, password):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()

    def validate_user(self, email, password):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {"user_id": row[0], "email": row[2]}  # Adjust index as per your table schema
        else:
            raise InvalidUserException("Invalid email or password")

    def get_user_expenses(self, user_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            raise ExpenseNotFoundException(f"No expenses found for user_id {user_id}")

        return [Expense(*row) for row in rows]

    def get_user_incomes(self, user_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM income WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Income(*row) for row in rows]

    def get_expense_categories(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expense_categories")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_income_categories(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM income_categories")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def add_expense(self, user_id, category_id, amount, date, description):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                       (user_id, category_id, amount, date, description))
        conn.commit()
        conn.close()

    def add_income(self, user_id, category_id, amount, date, description):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO income (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                       (user_id, category_id, amount, date, description))
        conn.commit()
        conn.close()

    def update_expense(self, expense_id, user_id, category_id, amount, date, description):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE expenses 
            SET category_id=?, amount=?, date=?, description=? 
            WHERE expense_id=? AND user_id=?
        """, (category_id, amount, date, description, expense_id, user_id))
        conn.commit()
        conn.close()

    def update_income(self, income_id, user_id, category_id, amount, date, description):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE income 
            SET category_id=?, amount=?, date=?, description=? 
            WHERE income_id=? AND user_id=?
        """, (category_id, amount, date, description, income_id, user_id))
        conn.commit()
        conn.close()

    def delete_expense(self, expense_id, user_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE expense_id=? AND user_id=?", (expense_id, user_id))
        conn.commit()
        conn.close()

    def delete_income(self, income_id, user_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM income WHERE income_id=? AND user_id=?", (income_id, user_id))
        conn.commit()
        conn.close()
