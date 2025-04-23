# entity/Inventory.py

from datetime import datetime
from entity.Product import Product

class Inventory:
    def __init__(self, inventory_id: int, product: Product, quantity_in_stock: int, last_stock_update=None):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update or datetime.now()

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity: int):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity: int):
        if self.is_product_available(quantity):
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
        else:
            print("❌ Not enough stock to remove.")

    def update_stock_quantity(self, new_quantity: int):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check: int):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.quantity_in_stock * self.product.get_price()

    def get_inventory_info(self):
        print(f"InventoryID: {self.inventory_id}, Product: {self.product.get_name()}, Stock: {self.quantity_in_stock}, Last Update: {self.last_stock_update}")
