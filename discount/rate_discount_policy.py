from discount.discount_policy import DiscountPolicy
from member.grade import Grade


class RateDiscountPolicy(DiscountPolicy):
    _discount_percent = 10

    def discount(self, member, price):
        if member.get_grade() == Grade.VIP:
            return int(price * self._discount_percent / 100)
        return 0
