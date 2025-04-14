import pyodbc

from dao.IFinanceRepository import IFinanceRepository
from util.DBConnUtil import DBConnUtil
from entity.Expense import Expense
from entity.User import User

class FinanceRepositoryImpl(IFinanceRepository):

    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def createUser(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                           (user.get_username(), user.get_password()))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error creating user:", e)
            return False

    def createExpense(self, expense):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (user_id, category, amount, date, description) 
                VALUES (?, ?, ?, ?, ?)
            """, (expense.get_user_id(), expense.get_category(), expense.get_amount(), 
                  expense.get_date(), expense.get_description()))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error creating expense:", e)
            return False

    def deleteUser(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error deleting user:", e)
            return False

    def deleteExpense(self, expense_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error deleting expense:", e)
            return False

    def getAllExpenses(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            expenses = []
            for row in rows:
                expense = Expense(row.id, row.user_id, row.category, row.amount, row.date, row.description)
                expenses.append(expense)
            return expenses
        except Exception as e:
            print("Error fetching expenses:", e)
            return []

    def updateExpense(self, user_id, expense):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE expenses 
                SET category = ?, amount = ?, date = ?, description = ? 
                WHERE id = ? AND user_id = ?
            """, (expense.get_category(), expense.get_amount(), expense.get_date(), 
                  expense.get_description(), expense.get_id(), user_id))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error updating expense:", e)
            return False
