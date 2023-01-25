from member.grade import Grade
from member.member import Member
from member.member_repository import MemberRepository
from member.member_service import MemberService


class MemberServiceImpl(MemberService):

    def __init__(self, member_repository):
        self.member_repository = member_repository

    def join(self, member):
        self.member_repository.save(member)

    def find_member(self, member_id):
        return self.member_repository.find_by_id(member_id)
