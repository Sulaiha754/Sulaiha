class Product:
    def __init__(self, product_id=None, name="", price=0.0, description="", stock_quantity=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def get_product_id(self):
        return self.product_id

    def __str__(self):
        return f"Product[ID={self.product_id}, Name={self.name}, Price={self.price}, Stock={self.stock_quantity}]"