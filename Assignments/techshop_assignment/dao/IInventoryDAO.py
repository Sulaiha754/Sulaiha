# dao/IInventoryDAO.py

from abc import ABC, abstractmethod
from entity.Inventory import Inventory

class IInventoryDAO(ABC):

    @abstractmethod
    def add_inventory(self, inventory: Inventory):
        pass

    @abstractmethod
    def get_all_inventory(self):
        pass

    @abstractmethod
    def update_inventory_quantity(self, inventory_id: int, new_quantity: int):
        pass

    @abstractmethod
    def get_inventory_by_product_id(self, product_id: int):
        pass
