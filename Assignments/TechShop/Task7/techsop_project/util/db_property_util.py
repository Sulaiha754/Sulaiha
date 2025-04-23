# Db Property Util.Py - Placeholder
def load_db_config(file_path):
    props = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    props[key.strip()] = value.strip()
    except Exception as e:
        print(f"Error loading DB config: {e}")
    return props
