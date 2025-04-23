
class InvalidAccountException(Exception):
    def __init__(self, message="The account number provided is invalid."):
        super().__init__(message)
