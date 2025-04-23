from entity.Order import Order
from entity.Product import Product

class OrderDetails:
    def __init__(self, order_detail_id=None, order=None, product=None, quantity=0, discount=0.0):
        self.order_detail_id = order_detail_id
        self.order = order  # Composition
        self.product = product  # Composition
        self.quantity = quantity
        self.discount = discount

    def calculate_subtotal(self):
        return self.quantity * self.product.price * (1 - self.discount)

    def get_order_detail_info(self):
        print(f"OrderDetailID: {self.order_detail_id}, Product: {self.product.name}, Quantity: {self.quantity}, Subtotal: {self.calculate_subtotal():.2f}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def add_discount(self, discount):
        self.discount = discount
