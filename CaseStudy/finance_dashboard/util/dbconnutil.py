import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        conn_str = DBPropertyUtil.get_connection_string('util/db.properties')
        return pyodbc.connect(conn_str)
