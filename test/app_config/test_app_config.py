from app_config import AppConfig


class TestAppConfig:
    def test_singleton(self):
        app_config = AppConfig()

        assert id(app_config.member_service().get_member_repository()) == id(app_config.member_repository())
        assert id(app_config.member_service().get_member_repository()) == id(app_config.order_service().get_member_repository())

