from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetails
from entity.Inventory import Inventory

from dao.CustomerDAOImpl import CustomerDAOImpl
from dao.ProductDAOImpl import ProductDAOImpl
from dao.OrderDAOImpl import OrderDAOImpl
from dao.OrderDetailsDAOImpl import OrderDetailsDAOImpl
from dao.InventoryDAOImpl import InventoryDAOImpl

from util.DBConnUtil import create_customers_table
from datetime import datetime

def main():
    # Ensure the 'customers' table exists
    create_customers_table()

    # Create instances of DAOs
    customer_dao = CustomerDAOImpl()
    product_dao = ProductDAOImpl()
    order_dao = OrderDAOImpl()
    order_details_dao = OrderDetailsDAOImpl()
    inventory_dao = InventoryDAOImpl()

    # Add a new customer
    new_customer = Customer(None, 'John Doe', 'john.doe@example.com', '123-456-7890')
    customer_dao.add_customer(new_customer)

    # Create a new product
    product = Product(name="Mouse", price=599.99, description="Wireless mouse", stock_quantity=50)
    product_dao.add_product(product)

    # Add product to inventory
    inventory = Inventory(
        inventory_id=None,
        product=product,
        quantity_in_stock=50,
        last_stock_update=datetime.now()
    )
    inventory_dao.add_inventory(inventory)

    # Use a valid customer (with ID 1)
    customer = Customer(1, 'John Doe', 'john.doe@example.com', '123-456-7890')

    # Create and add a new order
    order = Order(1, customer, datetime.now(), 500.0, "Processing")
    order_dao.add_order(order)

    # Add order detail
    order_detail = OrderDetails(
        order_detail_id=None,
        order=order,
        product=product,
        quantity=2,
        discount=0.1
    )
    order_details_dao.add_order_detail(order_detail)

    # --- Display All Data ---

    # Customers
    print("\n🧑‍🤝‍🧑 Customers:")
    customers = customer_dao.get_all_customers()
    for c in customers:
        print(c)

    # Products
    print("\n📦 Products:")
    all_products = product_dao.get_all_products()
    for p in all_products:
        print(p)

    # Orders with Details
    print("\n🧾 Orders and Order Details:")
    orders = order_dao.get_all_orders()
    for ord in orders:
        print(f"\n📦 Order ID: {ord.order_id} Details:")
        order_details = order_details_dao.get_order_details_by_order_id(ord.order_id)
        for detail in order_details:
            print(f"OrderDetailID: {detail[0]}, ProductID: {detail[2]}, Quantity: {detail[3]}, Discount: {detail[4]}")

    # Inventory
    print("\n📋 Inventory:")
    all_inventory = inventory_dao.get_all_inventory()
    for inv in all_inventory:
        print(f"InventoryID: {inv.inventory_id}, Product: {inv.product.name}, "
              f"Stock: {inv.quantity_in_stock}, Last Update: {inv.last_stock_update}")

if __name__ == "__main__":
    main()
