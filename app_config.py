from discount.rate_discount_policy import RateDiscountPolicy
from member.member_service_impl import MemberServiceImpl
from member.memory_member_repository import MemoryMemberRepository
from order.order_service_impl import OrderServiceImpl


class AppConfig:
    _store = {}
    
    def __init__(self):
        super().__init__()

    def get_bean(self, key):
        return self._store.get(key)

    def register(self, key, bean):
        if key not in self._store:
            self._store.update({key: bean})
        return self._store.get(key)

    def member_service(self):
        return self.register("member_service", MemberServiceImpl(self.member_repository()))

    def member_repository(self):
        return self.register("member_repository", MemoryMemberRepository())

    def order_service(self):
        return self.register("order_service", OrderServiceImpl(self.member_repository(), self.discount_policy()))

    def discount_policy(self):
        return self.register("discount_policy", RateDiscountPolicy())

