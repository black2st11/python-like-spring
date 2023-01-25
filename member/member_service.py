from abc import abstractmethod, ABCMeta


class MemberService(metaclass=ABCMeta):
    @abstractmethod
    def join(self, member):
        pass

    @abstractmethod
    def find_member(self, member_id):
        pass
