class Product:
    def __init__(self, product_id, product_name, description, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.category = category  # New field

    def __str__(self):
        return f"{self.product_name} - ${self.price} - Category: {self.category}"
