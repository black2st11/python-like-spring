from order.order import Order
from order.order_service import OrderService


class OrderServiceImpl(OrderService):

    def __init__(self, member_repository, discount_policy):
        self.member_repository = member_repository
        self.discount_policy = discount_policy

    def create_order(self, member_id, item_name, item_price):
        member = self.member_repository.find_by_id(member_id)
        discount = self.discount_policy.discount(member, item_price)
        return Order(member_id, item_name, item_price, discount)
