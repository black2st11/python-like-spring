from abc import abstractmethod, ABCMeta


class DiscountPolicy(metaclass=ABCMeta):
    @abstractmethod
    def discount(self, member, price):
        pass
