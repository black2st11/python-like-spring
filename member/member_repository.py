from abc import ABCMeta, abstractmethod


class MemberRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, member):
        pass

    @abstractmethod
    def find_by_id(self, member_id):
        pass


