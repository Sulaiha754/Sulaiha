# Db Conn Util.Py - Placeholder
import pyodbc
from util.db_property_util import load_db_config

def get_connection(config_file='techshop_db_config.properties'):
    config = load_db_config(config_file)
    try:
        conn_str = (
            f"DRIVER={config['driver']};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            f"Trusted_Connection={config['trusted_connection']};"
        )
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
