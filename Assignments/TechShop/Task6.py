# Product Class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        if self.stock_quantity + quantity < 0:
            raise ValueError(f"Insufficient stock for {self.name}")
        self.stock_quantity += quantity

# Order Class
class Order:
    def __init__(self, order_id, product, quantity, order_date, status='Pending'):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

# Payment Class
class Payment:
    def __init__(self, payment_id, order_id, amount, payment_date, status='Pending'):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.payment_date = payment_date
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

# Inventory Class
class Inventory:
    def __init__(self):
        self.products = {}  # product_id -> Product object

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product with this ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        del self.products[product_id]

    def update_product_stock(self, product_id, quantity):
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        self.products[product_id].update_stock(quantity)

    def get_product_by_id(self, product_id):
        return self.products.get(product_id, None)

    def get_products_by_category(self, category):
        return [p for p in self.products.values() if p.category == category]

    def search_products(self, search_term):
        return [p for p in self.products.values() if search_term.lower() in p.name.lower()]

# Orders Management
class OrderManager:
    def __init__(self):
        self.orders = []  # list of Order objects

    def add_order(self, order):
        if order.quantity > order.product.stock_quantity:
            raise ValueError("Not enough stock to fulfill the order.")
        order.product.update_stock(-order.quantity)  # Decrement product stock
        self.orders.append(order)

    def update_order_status(self, order_id, new_status):
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if order is None:
            raise ValueError("Order not found.")
        order.update_status(new_status)

    def remove_order(self, order_id):
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if order is None:
            raise ValueError("Order not found.")
        self.orders.remove(order)

    def get_orders_by_date(self, ascending=True):
        return sorted(self.orders, key=lambda o: o.order_date, reverse=not ascending)

# Payment Management
class PaymentManager:
    def __init__(self):
        self.payments = []  # list of Payment objects

    def add_payment(self, payment):
        self.payments.append(payment)

    def update_payment_status(self, payment_id, new_status):
        payment = next((p for p in self.payments if p.payment_id == payment_id), None)
        if payment is None:
            raise ValueError("Payment not found.")
        payment.update_status(new_status)

# Example Usage

# Initialize Inventory and OrderManager
inventory = Inventory()
order_manager = OrderManager()
payment_manager = PaymentManager()

# Adding products to inventory
product1 = Product(1, "Laptop", "Electronics", 1000, 50)
product2 = Product(2, "Smartphone", "Electronics", 500, 30)

inventory.add_product(product1)
inventory.add_product(product2)

# Add orders
order1 = Order(101, product1, 5, "2025-04-23")
order_manager.add_order(order1)

# Add payment for the order
payment1 = Payment(1001, order1.order_id, 5000, "2025-04-23")
payment_manager.add_payment(payment1)

# Update order status
order_manager.update_order_status(order1.order_id, "Shipped")

# Remove product from inventory
inventory.remove_product(2)

# Sort orders by date (ascending)
sorted_orders = order_manager.get_orders_by_date(ascending=True)

# Search products by name
search_results = inventory.search_products("Laptop")

# Update product stock
inventory.update_product_stock(1, -5)

# Display results
print(f"Sorted Orders by Date: {[o.order_id for o in sorted_orders]}")
print(f"Search Results for 'Laptop': {[p.name for p in search_results]}")
print(f"Remaining Stock for Laptop: {inventory.get_product_by_id(1).stock_quantity}")

