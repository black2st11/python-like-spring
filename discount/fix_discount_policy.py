from discount.discount_policy import DiscountPolicy
from member.grade import Grade


class FixDiscountPolicy(DiscountPolicy):
    _discount_fix_amount = 1000

    def discount(self, member, price):
        if member.get_grade() == Grade.VIP:
            return self._discount_fix_amount
        return 0
    