# Custom Exceptions

# Invalid Data Exception (for Data Validation)
class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Insufficient Stock Exception (for Inventory Management)
class InsufficientStockException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Incomplete Order Exception (for Order Processing)
class IncompleteOrderException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Payment Failed Exception (for Payment Processing)
class PaymentFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# IOException (for File I/O)
class IOException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# SQL Exception (for Database Access)
class SqlException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Concurrency Exception (for Concurrency Control)
class ConcurrencyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Authentication Exception (for Security)
class AuthenticationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Authorization Exception (for Security)
class AuthorizationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Create a User class that has the has_permission method
class User:
    def __init__(self, permissions):
        self.permissions = permissions  # A list of resources the user has access to

    def has_permission(self, resource):
        return resource in self.permissions

# Example Usage

def register_user(email):
    if "@" not in email or "." not in email:
        raise InvalidDataException("Invalid email address provided.")

def process_order(order, inventory):
    if order["quantity"] > inventory["stock"]:
        raise InsufficientStockException("Not enough stock to fulfill the order.")
    if not order["product"]:
        raise IncompleteOrderException("Order missing product details.")

def process_payment(order):
    # Simulate a payment failure
    payment_success = False
    if not payment_success:
        raise PaymentFailedException("Payment failed for the order.")

def write_to_log(log_data):
    try:
        with open("log.txt", "a") as file:
            file.write(log_data)
    except IOError:
        raise IOException("Error occurred while writing to the log file.")

def execute_sql_query(query):
    try:
        # Simulating a SQL query execution that fails
        raise Exception("Database is offline")
    except Exception as e:
        raise SqlException(f"SQL Error: {e}")

def update_order(order, new_details):
    # Simulating a concurrency control exception
    try:
        if order["status"] == "processing" and new_details["status"] == "shipped":
            raise ConcurrencyException("Conflict detected while updating the order.")
    except ConcurrencyException as e:
        print(f"Concurrency Error: {e}")

def authenticate_user(user, password):
    # Simulating failed authentication
    if not user or not password:
        raise AuthenticationException("Authentication failed. Invalid credentials.")

def authorize_user(user, resource):
    # Simulating failed authorization
    if not user.has_permission(resource):
        raise AuthorizationException(f"User does not have access to {resource}.")

# Example Calls

try:
    # Example 1: Invalid Email
    register_user("invalid-email.com")
except InvalidDataException as e:
    print(f"Error: {e}")

try:
    # Example 2: Insufficient Stock
    process_order({"quantity": 10, "product": "Laptop"}, {"stock": 5})
except InsufficientStockException as e:
    print(f"Error: {e}")

try:
    # Example 3: Incomplete Order
    process_order({"quantity": 2, "product": None}, {"stock": 10})
except IncompleteOrderException as e:
    print(f"Error: {e}")

try:
    # Example 4: Payment Failure
    process_payment({"order_id": 1001})
except PaymentFailedException as e:
    print(f"Error: {e}")

try:
    # Example 5: File I/O Exception
    write_to_log("Order processed successfully")
except IOException as e:
    print(f"Error: {e}")

try:
    # Example 6: SQL Exception
    execute_sql_query("SELECT * FROM orders")
except SqlException as e:
    print(f"Error: {e}")

try:
    # Example 7: Concurrency Error
    update_order({"status": "processing"}, {"status": "shipped"})
except ConcurrencyException as e:
    print(f"Error: {e}")

try:
    # Example 8: Authentication Error
    authenticate_user(None, "password123")
except AuthenticationException as e:
    print(f"Error: {e}")

# Example Usage with the User class
try:
    # Example 9: Authorization Error
    # Pass an instance of the User class, not a dictionary
    user = User(permissions=["user_dashboard", "orders"])  # A User object with permissions
    authorize_user(user, "admin_dashboard")  # This will raise AuthorizationException
except AuthorizationException as e:
    print(f"Error: {e}")
