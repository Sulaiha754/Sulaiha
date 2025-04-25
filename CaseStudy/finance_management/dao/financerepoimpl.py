from util.dbconnutil import DBConnUtil
from entity.expense import Expense
from entity.income import Income
from exception.expensenotfoundexception import ExpenseNotFoundException
from exception.invaliduserexception import InvalidUserException
from entity.user import User  # Assuming the User class is defined in entity.user


### financerepoimpl.py (Implementation)
import pyodbc
from dao.financerepo import FinanceRepo

class FinanceRepoImpl(FinanceRepo):
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=SULAI\\MSS,61896;DATABASE=financemanagerdb;Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def add_user(self, username, password, email):
        self.cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
   
    def add_income(self, user_id, category_id, amount, date, description):
        self.cursor.execute("INSERT INTO income (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                            (user_id, category_id, amount, date, description))
        self.conn.commit()

    def get_user_income(self, user_id):
        self.cursor.execute("SELECT * FROM income WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def update_income(self, income_id, category_id, amount, date, description):
        self.cursor.execute("UPDATE income SET category_id=?, amount=?, date=?, description=? WHERE income_id=?",
                            (category_id, amount, date, description, income_id))
        self.conn.commit()

    def delete_income(self, income_id):
        self.cursor.execute("DELETE FROM income WHERE income_id=?", (income_id,))
        self.conn.commit()

    def add_expense(self, user_id, category_id, amount, date, description):
        self.cursor.execute("INSERT INTO expenses (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                            (user_id, category_id, amount, date, description))
        self.conn.commit()

    def get_user_expenses(self, user_id):
        self.cursor.execute("SELECT * FROM expenses WHERE user_id=?", (user_id,))
        return self.cursor.fetchall()

    def update_expense(self, expense_id, category_id, amount, date, description):
        self.cursor.execute("UPDATE expenses SET category_id=?, amount=?, date=?, description=? WHERE expense_id=?",
                            (category_id, amount, date, description, expense_id))
        self.conn.commit()

    def delete_expense(self, expense_id):
        self.cursor.execute("DELETE FROM expenses WHERE expense_id=?", (expense_id,))
        self.conn.commit()

    def get_income_categories(self):
        self.cursor.execute("SELECT * FROM income_categories")
        return self.cursor.fetchall()

    def add_income_category(self, category_name):
        self.cursor.execute("INSERT INTO income_categories (category_name) VALUES (?)", (category_name,))
        self.conn.commit()

    def get_expense_categories(self):
        self.cursor.execute("SELECT * FROM expense_categories")
        return self.cursor.fetchall()

    def add_expense_category(self, category_name):
        self.cursor.execute("INSERT INTO expense_categories (category_name) VALUES (?)", (category_name,))
        self.conn.commit()

    def get_income_report(self, user_id):
        self.cursor.execute("SELECT SUM(amount) FROM income WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        return float(result[0]) if result[0] is not None else 0.0


    def get_expense_report(self, user_id):
        self.cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        return float(result[0]) if result[0] is not None else 0.0


    def get_income_category_id_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("select category_id from income_categories where category_name = ?", name)
        row = cursor.fetchone()
        return row[0] if row else None

    def get_expense_category_id_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("select category_id from expense_categories where category_name = ?", name)
        row = cursor.fetchone()
        return row[0] if row else None
    
    def get_all_income(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        select i.income_id, i.user_id, c.category_name, i.amount, i.date, i.description
        from income i join income_categories c on i.category_id = c.category_id
        where i.user_id = ?
        """, user_id)
        return cursor.fetchall()
    
    def get_all_expense(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
    select e.expense_id, e.user_id, c.category_name, e.amount, e.date, e.description
    from expenses e join expense_categories c on e.category_id = c.category_id
    where e.user_id = ?
    """, (user_id,))
        return cursor.fetchall()

        


