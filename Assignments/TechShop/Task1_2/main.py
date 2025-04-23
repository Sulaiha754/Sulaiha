from techshop_classes import Customer, Product, Order, OrderDetail, Inventory

# Step 1: Create a customer
customer = Customer(1, "Alice", "Smith", "alice@example.com", "9876543210", "42 Tech Park")

# Step 2: Create a product
product = Product(101, "Smartphone", "Latest model smartphone", 699.99)

# Step 3: Create inventory for the product
inventory = Inventory(1, product, 5)

# Step 4: Check stock and place order
if inventory.is_product_available(2):
    # Create an order
    order = Order(201, customer)

    # Create order detail
    order_detail = OrderDetail(301, order, product, 2)
    
    # Add order detail to order
    order.order_details.append(order_detail)
    
    # Calculate order total
    order.calculate_total_amount()

    # Remove stock
    inventory.remove_from_inventory(2)

    # Show order
    print("Customer Info:", customer.get_customer_details())
    print("Product Info:", product.get_product_details())
    print("Order Details:", order.get_order_details())
    print("Inventory After Order:", inventory.list_all_products())
else:
    print("Insufficient stock to place the order.")
