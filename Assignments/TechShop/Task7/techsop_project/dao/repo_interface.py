# Repo Interface.Py - Placeholder
from abc import ABC, abstractmethod

class TechShopRepo(ABC):
    @abstractmethod
    def add_customer(self, customer): pass

    @abstractmethod
    def get_customer_by_id(self, customer_id): pass

    @abstractmethod
    def update_customer_contact(self, customer_id, email, phone, address): pass

    @abstractmethod
    def add_product(self, product): pass

    @abstractmethod
    def add_product(self, product): pass  # Product now includes category


    @abstractmethod
    def get_product_by_id(self, product_id): pass

    @abstractmethod
    def update_product_price(self, product_id, new_price): pass

    @abstractmethod
    def create_order(self, order, order_details): pass

    @abstractmethod
    def get_order_status(self, order_id): pass


    @abstractmethod
    def get_inventory_by_product_id(self, product_id): pass

    @abstractmethod
    def update_inventory_quantity(self, product_id, quantity): pass
