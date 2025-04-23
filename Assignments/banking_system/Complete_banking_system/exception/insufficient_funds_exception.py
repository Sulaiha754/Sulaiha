
class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient balance in your account."):
        super().__init__(message)
