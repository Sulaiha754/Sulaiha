import sqlite3
from entity.Product import Product
from util.DBConnUtil import get_connection
from dao.IProductDAO import IProductDAO

class ProductDAOImpl(IProductDAO):
    def __init__(self):
        self.conn = get_connection()
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                stock_quantity INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, price, description, stock_quantity)
            VALUES (?, ?, ?, ?)
        ''', (product.name, product.price, product.description, product.stock_quantity))
        self.conn.commit()

    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        return [Product(*row) for row in rows]

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        row = cursor.fetchone()
        return Product(*row) if row else None

    def update_product(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE products 
            SET name = ?, price = ?, description = ?, stock_quantity = ? 
            WHERE product_id = ?
        ''', (product.name, product.price, product.description, product.stock_quantity, product.product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        self.conn.commit()
