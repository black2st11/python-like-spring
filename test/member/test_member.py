import pytest

from member.grade import Grade
from member.member import Member
from member.member_service_impl import MemberServiceImpl
from member.memory_member_repository import MemoryMemberRepository


class TestMember:

    @pytest.fixture(scope="function")
    def member_service(self):
        return MemberServiceImpl(MemoryMemberRepository())

    def test_join(self, member_service):
        member_id = 1
        member = Member(member_id, "memberA", Grade.VIP)
        member_service.join(member)
        result = member_service.find_member(member_id)

        assert member == result
