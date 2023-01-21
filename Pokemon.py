class Person:
    _age = 0
    height=0

    def __init__(self, name: str,height:int) -> None:
        self.name = name
        self.height = height

    def change_age(self, __increase_age, _age=None):
        self._age += __increase_age

class Doctor(Person):
    position_at_work=""
    def __init__(self,position_at_work=None,model=None,name=None,height=None):
        self.position_at_work=position_at_work
        super(Doctor).__init__(name,height)
        self.model=[name,height]
    def change_age(self,):
        super().change_age()






