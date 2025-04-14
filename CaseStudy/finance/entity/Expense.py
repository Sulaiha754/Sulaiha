class Expense:
    def __init__(self, id=None, user_id=None, category=None, amount=None, date=None, description=None):
        self.__id = id
        self.__user_id = user_id
        self.__category = category
        self.__amount = amount
        self.__date = date
        self.__description = description

    # Getters and Setters...
