
# db_config.py
import pyodbc

def get_connection():
    return pyodbc.connect(
       
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=SULAI\\MSS;"
"DATABASE=financemanagerdb;"
"Trusted_Connection=yes;"
)