# Incomplete Order Exception.Py - Placeholder
class IncompleteOrderException(Exception):
    def __init__(self, message="Order is incomplete or missing required details"):
        self.message = message
        super().__init__(self.message)
