# Customers Class
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        # Private attributes
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    # Getter methods
    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    # Setter methods with validation
    def set_email(self, email):
        if "@" not in email:
            print("Invalid email format!")
        else:
            self.__email = email

    def set_phone(self, phone):
        if len(phone) != 10:
            print("Phone number must be 10 digits!")
        else:
            self.__phone = phone

    def set_address(self, address):
        if len(address) < 10:
            print("Address should be at least 10 characters long!")
        else:
            self.__address = address

    # Method to display customer details
    def get_customer_details(self):
        print(f"CustomerID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, "
              f"Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}")


# Products Class
class Product:
    def __init__(self, product_id, product_name, description, price):
        # Private attributes
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    # Getter methods
    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    # Setter methods with validation
    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = price

    def set_description(self, description):
        if len(description) < 5:
            print("Description must be at least 5 characters long!")
        else:
            self.__description = description

    # Method to display product details
    def get_product_details(self):
        print(f"ProductID: {self.__product_id}, Name: {self.__product_name}, "
              f"Description: {self.__description}, Price: {self.__price}")


# Orders Class with Composition
class Order:
    def __init__(self, order_id, customer, order_date, total_amount):
        # Private attributes
        self.__order_id = order_id
        self.__customer = customer  # Composition (Order has a Customer)
        self.__order_date = order_date
        self.__total_amount = total_amount

    # Getter methods
    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    def get_customer(self):
        return self.__customer  # Returns the associated customer

    # Setter methods with validation
    def set_order_date(self, order_date):
        self.__order_date = order_date

    def set_total_amount(self, total_amount):
        if total_amount < 0:
            print("Total amount cannot be negative!")
        else:
            self.__total_amount = total_amount

    # Method to display order details
    def get_order_details(self):
        print(f"OrderID: {self.__order_id}, Customer: {self.__customer.get_first_name()} {self.__customer.get_last_name()}, "
              f"OrderDate: {self.__order_date}, TotalAmount: {self.__total_amount}")


# OrderDetails Class with Composition
class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        # Private attributes
        self.__order_detail_id = order_detail_id
        self.__order = order  # Composition (OrderDetail belongs to an Order)
        self.__product = product  # Composition (OrderDetail includes a Product)
        self.__quantity = quantity

    # Getter methods
    def get_order_detail_id(self):
        return self.__order_detail_id

    def get_quantity(self):
        return self.__quantity

    def get_order(self):
        return self.__order  # Returns the associated order

    def get_product(self):
        return self.__product  # Returns the associated product

    # Setter methods with validation
    def set_quantity(self, quantity):
        if quantity <= 0:
            print("Quantity must be a positive integer!")
        else:
            self.__quantity = quantity

    # Method to display order detail information
    def get_order_detail_info(self):
        print(f"OrderDetailID: {self.__order_detail_id}, OrderID: {self.__order.get_order_id()}, "
              f"Product: {self.__product.get_product_name()}, Quantity: {self.__quantity}")


# Inventory Class with Composition
class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        # Private attributes
        self.__inventory_id = inventory_id
        self.__product = product  # Composition (Inventory has a Product)
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    # Getter methods
    def get_inventory_id(self):
        return self.__inventory_id

    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_last_stock_update(self):
        return self.__last_stock_update

    # Setter methods with validation
    def set_quantity_in_stock(self, quantity_in_stock):
        if quantity_in_stock < 0:
            print("Quantity in stock cannot be negative!")
        else:
            self.__quantity_in_stock = quantity_in_stock

    # Method to add to inventory
    def add_to_inventory(self, quantity):
        self.__quantity_in_stock += quantity

    # Method to remove from inventory
    def remove_from_inventory(self, quantity):
        if quantity > self.__quantity_in_stock:
            print("Not enough stock to remove!")
        else:
            self.__quantity_in_stock -= quantity

    # Method to check if product is available
    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check

    # Method to display inventory details
    def get_inventory_details(self):
        print(f"InventoryID: {self.__inventory_id}, Product: {self.__product.get_product_name()}, "
              f"QuantityInStock: {self.__quantity_in_stock}, LastStockUpdate: {self.__last_stock_update}")


# Testing the composition

# Creating Customer
customer1 = Customer(1, "John", "Doe", "john.doe@example.com", "1234567890", "123 Elm Street")

# Creating Product
product1 = Product(101, "Laptop", "Gaming Laptop", 1500.00)

# Creating Order
order1 = Order(1001, customer1, "2025-04-23", 1500.00)

# Creating OrderDetail
order_detail1 = OrderDetail(1, order1, product1, 1)

# Creating Inventory
inventory1 = Inventory(1, product1, 10, "2025-04-22")

# Displaying Details
customer1.get_customer_details()
product1.get_product_details()
order1.get_order_details()
order_detail1.get_order_detail_info()
inventory1.get_inventory_details()
