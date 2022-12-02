class Pokemon:
    health=10
    power=10
    __level = 1
    def __init__(self,name:str)->None:
        self.name = name


    @property
    def level(self):
        return self.__level

    @property
    def stats(self):
        return {"health": self.health, "power": self.power}

    def up_xp(self, get_xp: int)->tuple[int,int]:
        self.xp +=get_xp
        amount = 0
        if self.__check_for_level_up():
            amount = self.__level_up()
        return self.xp, amount

    def __check_for_level_up(self):
        if self.xp >=REQUIRED_XP_FOR_LVL_UP:
            return True
        return False

    def __level_up(self) ->int:
        amount = self.xp
        self.__level += amount
        self.xp %= REQUIRED_XP_FOR_LVL_UP
        return amount
