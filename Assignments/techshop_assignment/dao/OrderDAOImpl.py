from util.DBConnUtil import get_connection
from entity.Order import Order
from entity.Customer import Customer

class OrderDAOImpl:
    def __init__(self):
        self.conn = get_connection()
        if self.conn:
            self.create_table()  # Create the table when OrderDAOImpl is initialized

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date TEXT,
            total_amount REAL,
            status TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()
        print("✅ Table 'orders' created or already exists.")

    def add_order(self, order: Order):
        query = '''
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (order.customer.get_customer_id(), order.order_date, order.total_amount, order.status))
        self.conn.commit()
        print("✅ Order inserted successfully.")

    def get_all_orders(self):
        cursor = self.conn.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        orders = []

        for row in rows:
            # Fetch the Customer object for each order using customer_id
            customer_cursor = self.conn.execute("SELECT * FROM customers WHERE customer_id = ?", (row[1],))
            customer_row = customer_cursor.fetchone()

            if customer_row:
                # Create the Customer object
                customer = Customer(customer_row[0], customer_row[1], customer_row[2], customer_row[3])
                # Create the Order object and associate it with the Customer
                order = Order(row[0], customer, row[2], row[3], row[4])
                orders.append(order)

        return orders

    def close(self):
        self.conn.close()
        print("🔒 Database connection closed.")
