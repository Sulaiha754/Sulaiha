from datetime import datetime
from entity.Customer import Customer

class Order:
    def __init__(self, order_id, customer: Customer, order_date=None, total_amount=0.0, status="Processing"):
        self.order_id = order_id
        self.customer = customer  # Composition: uses Customer object
        self.order_date = order_date if order_date else datetime.now()
        self.total_amount = total_amount
        self.status = status

    def calculate_total_amount(self, order_details):
        self.total_amount = sum(item['price'] * item['quantity'] for item in order_details)

    def get_order_details(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.get_name()}")
        print(f"Date: {self.order_date}")
        print(f"Status: {self.status}")
        print(f"Total Amount: ₹{self.total_amount:.2f}")

    def update_order_status(self, new_status):
        self.status = new_status
        print(f"🔁 Order status updated to '{new_status}'.")

    def cancel_order(self):
        self.status = "Cancelled"
        print("❌ Order has been cancelled.")
