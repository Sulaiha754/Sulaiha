import configparser

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(file_name):
        config = configparser.ConfigParser()
        config.read(file_name)
        return config['database']['connection_string']
