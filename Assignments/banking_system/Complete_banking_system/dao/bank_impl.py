from util.db_conn_util import DBConnUtil
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.invalid_account_exception import InvalidAccountException
from dao.bank_interface import IBankServiceProvider

class BankServiceImpl(IBankServiceProvider):
    def create_account(self, customer, account_type, balance):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()

        # Insert customer (customer_id is auto-generated)
        insert_customer = """
        INSERT INTO Customers (first_name, last_name, dob, email, phone_number, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_customer,
                       customer.first_name, customer.last_name, customer.dob,
                       customer.email, customer.phone_number, customer.address)

        # Get the new customer_id
        cursor.execute("SELECT SCOPE_IDENTITY()")
        customer_id = cursor.fetchone()[0]

        # Insert account
        insert_account = """
            INSERT INTO Accounts (customer_id, account_type, balance)
            VALUES (?, ?, ?)
        """
        cursor.execute(insert_account, customer_id, account_type, balance)

        # Get the new account_id
        cursor.execute("SELECT SCOPE_IDENTITY()")
        account_id = cursor.fetchone()[0]

        conn.commit()
        print("Account created successfully.")
        print(f"Account ID: {account_id}")
        print(f"Customer ID: {customer_id}")

        return account_id, customer_id

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
        if row[0] < amount:
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
        return result[0]

    def get_account_details(self, account_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.first_name, c.last_name, a.account_type, a.balance 
            FROM Accounts a 
            JOIN Customers c ON a.customer_id = c.customer_id 
            WHERE a.account_id = ?
        """, account_id)
        return cursor.fetchone()
