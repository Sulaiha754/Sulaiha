#Tas1:Class and their Attributes
# techshop_classes.py
from datetime import datetime

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.orders = []

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return vars(self)

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = True

    def get_product_details(self):
        return vars(self)

    def update_product_info(self, description=None, price=None):
        if description:
            self.description = description
        if price is not None:
            self.price = price

    def is_product_in_stock(self):
        return self.in_stock

class Order:
    def __init__(self, order_id, customer, order_date=None):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date if order_date else datetime.now()
        self.total_amount = 0
        self.status = "Processing"
        self.order_details = []

    def calculate_total_amount(self):
        self.total_amount = sum([od.calculate_subtotal() for od in self.order_details])
        return self.total_amount

    def get_order_details(self):
        return {
            "OrderID": self.order_id,
            "Customer": self.customer.get_customer_details(),
            "TotalAmount": self.total_amount,
            "Status": self.status,
            "OrderDate": self.order_date,
            "Items": [od.get_order_detail_info() for od in self.order_details]
        }

    def update_order_status(self, new_status):
        self.status = new_status

    def cancel_order(self):
        self.status = "Cancelled"
        for od in self.order_details:
            od.product.in_stock = True

class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity
        self.discount = 0

    def calculate_subtotal(self):
        return (self.product.price * self.quantity) * (1 - self.discount)

    def get_order_detail_info(self):
        return {
            "Product": self.product.get_product_details(),
            "Quantity": self.quantity,
            "Subtotal": self.calculate_subtotal()
        }

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def add_discount(self, discount):
        self.discount = discount

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update=None):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update if last_stock_update else datetime.now()

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
        else:
            raise ValueError("Insufficient stock")

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        return self.product if self.quantity_in_stock < threshold else None

    def list_out_of_stock_products(self):
        return self.product if self.quantity_in_stock == 0 else None

    def list_all_products(self):
        return {
            "Product": self.product.get_product_details(),
            "Quantity": self.quantity_in_stock
        }
