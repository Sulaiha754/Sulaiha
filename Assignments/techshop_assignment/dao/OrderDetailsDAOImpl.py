from util.DBConnUtil import get_connection
from entity.OrderDetails import OrderDetails
from entity.Product import Product
from entity.Order import Order

class OrderDetailsDAOImpl:
    def __init__(self):
        self.conn = get_connection()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS order_details (
            order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            discount REAL,
            FOREIGN KEY(order_id) REFERENCES orders(order_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()
        print("✅ Table 'order_details' created or already exists.")

    def add_order_detail(self, order_detail: OrderDetails):
        query = '''
        INSERT INTO order_details (order_id, product_id, quantity, discount)
        VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (
            order_detail.order.order_id,
            order_detail.product.product_id,
            order_detail.quantity,
            order_detail.discount
        ))
        self.conn.commit()
        print("✅ Order detail inserted successfully.")

    def get_order_details_by_order_id(self, order_id):
        cursor = self.conn.execute(
            "SELECT order_detail_id, order_id, product_id, quantity, discount FROM order_details WHERE order_id = ?",
            (order_id,))
        return cursor.fetchall()
