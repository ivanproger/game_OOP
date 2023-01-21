class Weapon:   интерфейсы
    health = [10]
    damage = [10]

    def __init__(self, user):
        self.user = user

    def attach(self,user):
        raise NotImplementedError

class Sword(Weapon):

    def attach(self,user):
             print("Меч рубит")

class Spear(Weapon):

    def attach(self,user):
          print("копьё колит")
class Bow(Weapon):
    pass