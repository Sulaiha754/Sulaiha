from abc import ABC, abstractmethod

class IOrderDetailsDAO(ABC):

    @abstractmethod
    def add_order_detail(self, order_detail): pass

    @abstractmethod
    def get_order_details_by_order_id(self, order_id): pass
