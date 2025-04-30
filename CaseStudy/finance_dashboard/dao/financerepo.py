from abc import ABC, abstractmethod

class FinanceRepo(ABC):
    
    @abstractmethod
    def register_user(self, username, email, password): pass

    @abstractmethod
    def validate_user(self, username, password): pass

    @abstractmethod
    def get_user_expenses(self, user_id): pass

    @abstractmethod
    def get_user_incomes(self, user_id): pass

    @abstractmethod
    def get_expense_categories(self): pass

    @abstractmethod
    def get_income_categories(self): pass


    @abstractmethod
    def add_expense(self, user_id, category_id, amount, date, description): pass

    @abstractmethod
    def add_income(self, user_id, category_id, amount, date, description): pass

    @abstractmethod
    def update_expense(self, expense_id, category_id, amount, date, description): pass

    @abstractmethod
    def update_income(self, income_id, category_id, amount, date, description): pass

    @abstractmethod
    def delete_expense(self, expense_id): pass

    @abstractmethod
    def delete_income(self, income_id): pass
