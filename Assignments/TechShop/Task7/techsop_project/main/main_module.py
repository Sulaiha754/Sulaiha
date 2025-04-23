# Main Module.Py - Placeholder
from entity.customer import Customer
from entity.product import Product
from entity.order import Order
from entity.order_detail import OrderDetail
from dao.repo_impl import TechShopRepoImpl
from datetime import datetime

def print_menu():
    print("\n==== TechShop - Electronic Gadgets ====")
    print("1. Register New Customer")
    print("2. Add New Product")
    print("3. Place Order")
    print("4. Track Order Status")
    print("5. Exit")


def register_customer(repo):
    try:
        cid = int(input("Customer ID: "))
        fname = input("First Name: ")
        lname = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")

        customer = Customer(cid, fname, lname, email, phone, address)
        repo.add_customer(customer)
        print("Customer registered successfully!")
    except Exception as e:
        print(f"Error: {e}")

def add_product(repo):
    try:
        pid = int(input("Product ID: "))
        name = input("Product Name: ")
        desc = input("Description: ")
        price = float(input("Price: "))
        category = input("Category: ")

        product = Product(pid, name, desc, price, category)
        repo.add_product(product)
        print("Product added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def place_order(repo):
    try:
        oid = int(input("Order ID: "))
        cid = int(input("Customer ID: "))
        date = input("Order Date (YYYY-MM-DD): ")
        num_items = int(input("Number of items: "))
        total = 0
        details = []

        for i in range(num_items):
            odid = int(input("  Order Detail ID: "))
            pid = int(input("  Product ID: "))
            qty = int(input("  Quantity: "))
            product = repo.get_product_by_id(pid)
            if not product:
                print(f"  Product ID {pid} not found!")
                continue
            price = float(product.Price)
            subtotal = qty * price
            total += subtotal
            details.append(OrderDetail(odid, oid, pid, qty))

        order = Order(oid, cid, date, total)
        repo.create_order(order, details)
        print("Order placed successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    repo = TechShopRepoImpl()

    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            register_customer(repo)
        elif choice == "2":
            add_product(repo)
        elif choice == "3":
            place_order(repo)
        elif choice == "4":
            order_id = input("Enter Order ID to track: ")
            try:
                status = repo.get_order_status(order_id)
                print(f"Order Status: {status}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
