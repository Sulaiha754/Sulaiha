from abc import ABC, abstractmethod
from entity.Order import Order

class IOrderDAO(ABC):

    @abstractmethod
    def add_order(self, order: Order):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def get_order_by_id(self, order_id):
        pass

    @abstractmethod
    def update_order(self, order: Order):
        pass

    @abstractmethod
    def delete_order(self, order_id):
        pass
