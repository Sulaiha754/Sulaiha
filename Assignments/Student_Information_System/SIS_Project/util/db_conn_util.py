import pyodbc
from util.db_property_util import get_connection_string

class DBConnUtil:
    @staticmethod
    def get_connection():
        conn_str = get_connection_string()
        return pyodbc.connect(conn_str)
