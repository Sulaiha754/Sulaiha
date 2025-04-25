
### financerepo.py (Interface)
from abc import ABC, abstractmethod

class FinanceRepo(ABC):

    @abstractmethod
    def add_user(self, username, password, email): pass

    @abstractmethod
    def get_all_users(self): pass

    @abstractmethod
    def add_income(self, user_id, category_id, amount, date, description): pass

    @abstractmethod
    def get_user_income(self, user_id): pass

    @abstractmethod
    def update_income(self, income_id, category_id, amount, date, description): pass

    @abstractmethod
    def delete_income(self, income_id): pass

    @abstractmethod
    def add_expense(self, user_id, category_id, amount, date, description): pass

    @abstractmethod
    def get_user_expenses(self, user_id): pass

    @abstractmethod
    def update_expense(self, expense_id, category_id, amount, date, description): pass

    @abstractmethod
    def delete_expense(self, expense_id): pass

    @abstractmethod
    def get_income_categories(self): pass

    @abstractmethod
    def add_income_category(self, category_name): pass

    @abstractmethod
    def get_expense_categories(self): pass

    @abstractmethod
    def add_expense_category(self, category_name): pass

    @abstractmethod
    def get_income_report(self, user_id): pass

    @abstractmethod
    def get_expense_report(self, user_id): pass
    @abstractmethod
    def get_income_category_id_by_name(self, name): pass

    @abstractmethod
    def get_expense_category_id_by_name(self, name): pass
