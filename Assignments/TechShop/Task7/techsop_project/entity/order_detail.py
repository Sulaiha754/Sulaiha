# Order Detail.Py - Placeholder
class OrderDetail:
    def __init__(self, order_detail_id, order_id, product_id, quantity):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return f"Detail #{self.order_detail_id} for Order #{self.order_id}, Product #{self.product_id}"
