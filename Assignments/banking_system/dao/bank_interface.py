
from abc import ABC, abstractmethod

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, account_type, balance): pass

    @abstractmethod
    def deposit(self, account_id, amount): pass

    @abstractmethod
    def withdraw(self, account_id, amount): pass

    @abstractmethod
    def get_balance(self, account_id): pass

    @abstractmethod
    def get_account_details(self, account_id): pass
