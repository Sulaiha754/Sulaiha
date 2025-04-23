from dao.IInventoryDAO import IInventoryDAO
from entity.Inventory import Inventory
from entity.Product import Product
from util.DBConnUtil import get_connection

class InventoryDAOImpl(IInventoryDAO):
    def __init__(self):
        self.conn = get_connection()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity_in_stock INTEGER,
            last_stock_update TEXT,
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
        '''
        self.conn.execute(query)
        self.conn.commit()
        print("✅ Table 'inventory' created or already exists.")

    def add_inventory(self, inventory: Inventory):
        query = '''
        INSERT INTO inventory (product_id, quantity_in_stock, last_stock_update)
        VALUES (?, ?, ?)
        '''
        self.conn.execute(query, (inventory.product.get_product_id(), inventory.quantity_in_stock, inventory.last_stock_update))
        self.conn.commit()
        print("✅ Inventory item added successfully.")

    def get_all_inventory(self):
        cursor = self.conn.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        inventory_list = []
        for row in rows:
            # Fetch product details for the product_id
            product_cursor = self.conn.execute("SELECT * FROM products WHERE product_id = ?", (row[1],))
            product_row = product_cursor.fetchone()
            if product_row:
                product = Product(
                    product_id=product_row[0],
                    name=product_row[1],
                    price=product_row[2],
                    description=product_row[3],
                    stock_quantity=product_row[4]
                )
                inventory = Inventory(row[0], product, row[2], row[3])
                inventory_list.append(inventory)
        return inventory_list

    def update_inventory_quantity(self, inventory_id: int, new_quantity: int):
        query = "UPDATE inventory SET quantity_in_stock = ?, last_stock_update = datetime('now') WHERE inventory_id = ?"
        self.conn.execute(query, (new_quantity, inventory_id))
        self.conn.commit()
        print("✅ Inventory quantity updated.")

    def get_inventory_by_product_id(self, product_id: int):
        cursor = self.conn.execute("SELECT * FROM inventory WHERE product_id = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product_cursor = self.conn.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
            product_row = product_cursor.fetchone()
            if product_row:
                product = Product(
                    product_id=product_row[0],
                    name=product_row[1],
                    price=product_row[2],
                    description=product_row[3],
                    stock_quantity=product_row[4]
                )
                return Inventory(row[0], product, row[2], row[3])
        return None

    def list_low_stock_products(self, threshold: int):
        cursor = self.conn.execute("SELECT * FROM inventory WHERE quantity_in_stock < ?", (threshold,))
        rows = cursor.fetchall()
        low_stock_list = []
        for row in rows:
            # Fetch product details for each low stock item
            product_cursor = self.conn.execute("SELECT * FROM products WHERE product_id = ?", (row[1],))
            product_row = product_cursor.fetchone()
            if product_row:
                product = Product(
                    product_id=product_row[0],
                    name=product_row[1],
                    price=product_row[2],
                    description=product_row[3],
                    stock_quantity=product_row[4]
                )
                inventory = Inventory(row[0], product, row[2], row[3])
                low_stock_list.append(inventory)
        return low_stock_list

    def list_out_of_stock_products(self):
        cursor = self.conn.execute("SELECT * FROM inventory WHERE quantity_in_stock = 0")
        rows = cursor.fetchall()
        out_of_stock_list = []
        for row in rows:
            # Fetch product details for each out-of-stock item
            product_cursor = self.conn.execute("SELECT * FROM products WHERE product_id = ?", (row[1],))
            product_row = product_cursor.fetchone()
            if product_row:
                product = Product(
                    product_id=product_row[0],
                    name=product_row[1],
                    price=product_row[2],
                    description=product_row[3],
                    stock_quantity=product_row[4]
                )
                inventory = Inventory(row[0], product, row[2], row[3])
                out_of_stock_list.append(inventory)
        return out_of_stock_list

    def list_all_products(self):
        cursor = self.conn.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        all_products_list = []
        for row in rows:
            # Fetch product details for each item
            product_cursor = self.conn.execute("SELECT * FROM products WHERE product_id = ?", (row[1],))
            product_row = product_cursor.fetchone()
            if product_row:
                product = Product(
                    product_id=product_row[0],
                    name=product_row[1],
                    price=product_row[2],
                    description=product_row[3],
                    stock_quantity=product_row[4]
                )
                inventory = Inventory(row[0], product, row[2], row[3])
                all_products_list.append(inventory)
        return all_products_list
