class Member:
    def __init__(self, id, name, grade):
        self._id = id
        self._name = name
        self._grade = grade

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

    def __str__(self):
        return f"id = {self._id}, name = {self._name}, grade = {self._grade}"
