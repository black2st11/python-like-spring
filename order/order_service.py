from abc import ABCMeta, abstractmethod


class OrderService(metaclass=ABCMeta):
    @abstractmethod
    def create_order(self, member_id, item_name, item_price):
        pass