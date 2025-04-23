# Repo Impl.Py - Placeholder
import pyodbc
from util.db_conn_util import get_connection
from exception.invalid_data_exception import InvalidDataException

class TechShopRepoImpl:
    def __init__(self):
        self.conn = get_connection()

    def add_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)",
                (customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone, customer.address)
            )
            self.conn.commit()
        except Exception as e:
            raise InvalidDataException(f"Error adding customer: {e}")

    def get_customer_by_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
        return cursor.fetchone()

    def update_customer_contact(self, customer_id, email, phone, address):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE Customers SET Email = ?, Phone = ?, Address = ? WHERE CustomerID = ?",
            (email, phone, address, customer_id)
        )
        self.conn.commit()

    def add_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute(
    "INSERT INTO Products (ProductID, ProductName, Description, Price, Category) VALUES (?, ?, ?, ?, ?)",
    (product.product_id, product.product_name, product.description, product.price, product.category)
 )
        self.conn.commit()

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
        return cursor.fetchone()

    def update_product_price(self, product_id, new_price):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Products SET Price = ? WHERE ProductID = ?", (new_price, product_id))
        self.conn.commit()

    def create_order(self, order, order_details):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)",
            (order.order_id, order.customer_id, order.order_date, order.total_amount)
        )
        for detail in order_details:
            cursor.execute(
                "INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)",
                (detail.order_detail_id, detail.order_id, detail.product_id, detail.quantity)
            )
        self.conn.commit()

    def get_order_status(self, order_id):
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT Status FROM Orders WHERE OrderID = ?", (order_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    raise Exception("Order ID not found.")
            except Exception as e:
                raise e


    def get_inventory_by_product_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Inventory WHERE ProductID = ?", (product_id,))
        return cursor.fetchone()

    def update_inventory_quantity(self, product_id, quantity):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Inventory SET QuantityInStock - ? WHERE ProductID = ?", (quantity, product_id))
        self.conn.commit()


