class Customer:
    def __init__(self, customer_id, name, email, phone):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone = phone

    # Getters
    def get_customer_id(self):
        return self._customer_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    # Setters
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return f"Customer[ID={self._customer_id}, Name={self._name}, Email={self._email}, Phone={self._phone}]"
