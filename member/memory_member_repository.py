from member.member_repository import MemberRepository


class MemoryMemberRepository(MemberRepository):
    _store = {}

    def save(self, member):
        self._store.update({member.get_id(): member})

    def find_by_id(self, member_id):
        return self._store.get(member_id)
