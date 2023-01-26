from app_config import AppConfig
from member.grade import Grade
from member.member import Member
from member.member_repository import MemberRepository
from member.memory_member_repository import MemoryMemberRepository


class TestAppConfig:
    def test_singleton(self):
        app_config = AppConfig()

        assert id(app_config.member_service().get_member_repository()) == id(app_config.member_repository())
        assert id(app_config.member_service().get_member_repository()) == id(app_config.order_service().get_member_repository())

