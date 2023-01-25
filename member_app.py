from member.grade import Grade
from member.member import Member
from member.member_service_impl import MemberServiceImpl
from member.memory_member_repository import MemoryMemberRepository


class MemberApp:
    @staticmethod
    def start():
        member_id = 1
        member_service = MemberServiceImpl(MemoryMemberRepository)
        member = Member(member_id, "memberA", Grade.VIP)

        member_service.join(member)

        result = member_service.find_member(member_id)

        print("member = " + member.__str__())
        print("result = " + result.__str__())


MemberApp().start()
