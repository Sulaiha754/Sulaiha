import os
import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, 'db.properties')  # Absolute path
        conn_str = DBPropertyUtil.get_connection_string(config_path)
        return pyodbc.connect(conn_str)
