import pytest

from discount.fix_discount_policy import FixDiscountPolicy
from member.grade import Grade
from member.member import Member
from member.member_service_impl import MemberServiceImpl
from member.memory_member_repository import MemoryMemberRepository
from order.order_service_impl import OrderServiceImpl


class TestOrder:

    @pytest.fixture(scope="function")
    def member_repository(self):
        return MemoryMemberRepository()

    @pytest.fixture(scope="function")
    def member_service(self, member_repository):
        return MemberServiceImpl(member_repository)

    @pytest.fixture(scope="function")
    def order_service(self, member_repository):
        return OrderServiceImpl(member_repository, FixDiscountPolicy())

    def test_create_order(self, member_service, order_service):
        member_id = 1
        member = Member(member_id, "memberA", Grade.VIP)
        member_service.join(member)

        order = order_service.create_order(member_id, "itemA", 10000)

        assert order.get_discount_price() == 1000
