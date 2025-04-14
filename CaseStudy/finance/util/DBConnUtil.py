import pyodbc
from util.DBPropertyUtil import get_connection_string

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            conn_str = get_connection_string()
            return pyodbc.connect(conn_str)
        except Exception as e:
            print("Error connecting to DB:", e)
            return None
