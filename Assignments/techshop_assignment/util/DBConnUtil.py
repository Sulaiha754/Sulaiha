import sqlite3

def get_connection():
    # Ensure the database file path is correct relative to your project directory
    return sqlite3.connect('techshop.db')

def create_customers_table():
    conn = get_connection()  # Connect to the database
    cursor = conn.cursor()

    # Create the 'customers' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        );
    """)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
