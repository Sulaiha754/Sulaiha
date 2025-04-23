# Order.Py - Placeholder
class Order:
    def __init__(self, order_id, customer_id, order_date, total_amount):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount

    def __str__(self):
        return f"Order #{self.order_id} by Customer {self.customer_id} on {self.order_date}"
