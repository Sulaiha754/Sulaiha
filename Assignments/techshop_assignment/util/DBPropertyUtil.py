def load_db_properties():
    props = {}
    with open('db.properties', 'r') as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                props[key.strip()] = value.strip()
    return props
