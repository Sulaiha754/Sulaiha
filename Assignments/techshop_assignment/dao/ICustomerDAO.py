from abc import ABC, abstractmethod
from entity.Customer import Customer

class ICustomerDAO(ABC):

    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int):
        pass

    @abstractmethod
    def update_customer(self, customer: Customer):
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int):
        pass
