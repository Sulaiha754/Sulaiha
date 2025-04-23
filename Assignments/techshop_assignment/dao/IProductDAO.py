from abc import ABC, abstractmethod
from entity.Product import Product

class IProductDAO(ABC):

    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def update_product(self, product: Product):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass
