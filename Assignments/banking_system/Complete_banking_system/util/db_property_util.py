import configparser

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(file_name):
        config = configparser.ConfigParser()
        print(f"Reading properties file: {file_name}")  # Debug
        read_files = config.read(file_name)
        print(f"Files read: {read_files}")  # Debug
        print(f"Sections found: {config.sections()}")  # Debug
        return config['database']['connection_string']
