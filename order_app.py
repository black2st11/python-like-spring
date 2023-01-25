from discount.fix_discount_policy import FixDiscountPolicy
from member.grade import Grade
from member.member import Member
from member.member_service_impl import MemberServiceImpl
from member.memory_member_repository import MemoryMemberRepository
from order.order_service_impl import OrderServiceImpl


class OrderApp:
    def start(self):
        memory_repository= MemoryMemberRepository()
        member_service = MemberServiceImpl(memory_repository)
        order_service = OrderServiceImpl(memory_repository, FixDiscountPolicy())
        member_id = 1
        member = Member(member_id, "memberA", Grade.VIP)
        member_service.join(member)

        order = order_service.create_order(member_id, "itemA", 10000)

        print(order)

OrderApp().start()