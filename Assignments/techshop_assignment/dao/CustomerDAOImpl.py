import sqlite3
from entity.Customer import Customer
from util.DBConnUtil import get_connection
from exception.InvalidDataException import InvalidDataException
from dao.ICustomerDAO import ICustomerDAO

class CustomerDAOImpl(ICustomerDAO):

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise InvalidDataException("Invalid customer object")

        conn = get_connection()
        cursor = conn.cursor()

        # Insert a new customer into the 'customers' table
        cursor.execute("""
            INSERT INTO customers (name, email, phone)
            VALUES (?, ?, ?)
        """, (customer.get_name(), customer.get_email(), customer.get_phone()))
        conn.commit()
        conn.close()

    def get_all_customers(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        conn.close()

        return [Customer(*row) for row in rows]

    def get_customer_by_id(self, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Customer(*row)
        else:
            return None

    def update_customer(self, customer):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE customers 
            SET name = ?, email = ?, phone = ? 
            WHERE customer_id = ?
        """, (customer.get_name(), customer.get_email(), customer.get_phone(), customer.get_customer_id()))
        conn.commit()
        conn.close()

    def delete_customer(self, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        conn.commit()
        conn.close()
