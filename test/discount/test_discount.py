import pytest

from discount.fix_discount_policy import FixDiscountPolicy
from discount.rate_discount_policy import RateDiscountPolicy
from member.grade import Grade
from member.member import Member


class TestDiscount:

    @pytest.fixture(scope='function')
    def vip_member(self):
        return Member(1, 'memberA', Grade.VIP)

    @pytest.fixture(scope='function')
    def basic_member(self):
        return Member(2, 'memberB', Grade.BASIC)

    def test_fix_discount(self, vip_member, basic_member):
        fix_discount_policy = FixDiscountPolicy()
        discount1 = fix_discount_policy.discount(vip_member, 10000)
        discount2 = fix_discount_policy.discount(vip_member, 20000)
        discount3 = fix_discount_policy.discount(basic_member, 10000)
        assert discount1 == 1000
        assert discount2 == 1000
        assert discount3 == 0

    def test_rate_discount(self, vip_member, basic_member):
        rate_discount_policy = RateDiscountPolicy()
        discount1 = rate_discount_policy.discount(vip_member, 10000)
        discount2 = rate_discount_policy.discount(vip_member, 20000)
        discount3 = rate_discount_policy.discount(basic_member, 10000)

        assert discount1 == 1000
        assert discount2 == 2000
        assert discount3 == 0
