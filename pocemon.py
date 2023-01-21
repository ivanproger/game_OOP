REQUIRED_XP_FOR_LVL_UP = 12
import random


class Pokemon:
    __health = 10
    __power = 10
    __level = 1
    __xp = 0
    __combo = 0
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def level(self):
        return self.__level

    @property
    def stats(self):
        return {"health": self.__health, "power": self.__power, "level": self.__level, "xp": self.__xp,
                "combo": self.__combo}

    def up_xp(self, get_xp: int) -> tuple[int, int]:
        self.__xp += get_xp
        amount = 0

        if self.__check_for_level_up(REQUIRED_XP_FOR_LVL_UP):
            amount = self.__level_up(REQUIRED_XP_FOR_LVL_UP)
        return self.__xp, self.__level

    def __check_for_level_up(self, REQUIRED_XP_FOR_LVL_UP: int):
        if self.__xp >= REQUIRED_XP_FOR_LVL_UP:
            return True
        return False

    def __level_up(self, REQUIRED_XP_FOR_LVL_UP: int) -> int:
        amount = self.__xp // REQUIRED_XP_FOR_LVL_UP
        self.__level += amount
        self.__xp %= REQUIRED_XP_FOR_LVL_UP
        return amount

    def attack(self, fighter: object):
            fighter_1=random.randint(0,self.stats["health"]+self.stats["power"]+self.stats["level"]*self.stats["combo"])
            fighter_2=random.randint(0,fighter.stats["health"]+fighter.stats["power"]+fighter.stats["level"]*fighter.stats["combo"])
            if fighter_1>fighter_2:
                health=random.randint(0,3)
                power=random.randint(0,3)
                fighter.__health-=health
                self.__power+=power
                combo=random.randint(0,1)
                self.__combo+=combo
                fighter.__combo=0

                return "WIN1"
            if fighter_2>fighter_1:
                health=random.randint(0,3)
                power=random.randint(0,3)
                self.__health-=health
                fighter.__power+=power
                combo=random.randint(0,1)
                fighter.__combo+=combo
                self.__combo=0
                return "WIN2"
            if fighter_1==fighter_2:
                return "cool"

