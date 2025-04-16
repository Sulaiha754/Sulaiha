
from util.db_conn_util import DBConnUtil
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.invalid_account_exception import InvalidAccountException
from dao.bank_interface import IBankServiceProvider

class BankServiceImpl(IBankServiceProvider):
    def create_account(self, customer, account_type, balance):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customers (first_name, last_name, dob, email, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)",
                       customer.first_name, customer.last_name, customer.dob, customer.email, customer.phone_number, customer.address)
        customer_id = cursor.execute("SELECT @@IDENTITY").fetchval()

        cursor.execute("INSERT INTO Accounts (customer_id, account_type, balance) VALUES (?, ?, ?)",
                       customer_id, account_type, balance)
        conn.commit()
        print("Account created successfully.")

    def deposit(self, account_id, amount):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", amount, account_id)
        conn.commit()
        print("Deposit successful.")

    def withdraw(self, account_id, amount):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", account_id)
        row = cursor.fetchone()
        if not row:
            raise InvalidAccountException()
        if row.balance < amount:
            raise InsufficientFundsException()
        cursor.execute("UPDATE Accounts SET balance = balance - ? WHERE account_id = ?", amount, account_id)
        conn.commit()
        print("Withdrawal successful.")

    def get_balance(self, account_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", account_id)
        result = cursor.fetchone()
        if not result:
            raise InvalidAccountException()
        return result.balance

    def get_account_details(self, account_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.first_name, c.last_name, a.account_type, a.balance 
            FROM Accounts a 
            JOIN Customers c ON a.customer_id = c.customer_id 
            WHERE a.account_id = ?""", account_id)
        return cursor.fetchone()
