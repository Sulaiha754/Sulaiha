# Insufficient Stock Exception.Py - Placeholder
class InsufficientStockException(Exception):
    def __init__(self, message="Not enough stock available"):
        self.message = message
        super().__init__(self.message)
