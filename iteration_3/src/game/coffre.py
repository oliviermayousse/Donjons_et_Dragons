from .base import BaseName, BaseCompetence


class Coffre(BaseName, BaseCompetence):

    def __init__(self, name, image, case, life, attack_level):
        BaseName.__init__(self, name)
        BaseCompetence.__init__(self, image, life, attack_level)
        self.case = case


    @classmethod
    def get_list_coffre(cls):
        list_coffre = [
            cls("Arc", "\033[34m🏹\033[0m", 2, 0, 1),
            cls("Arc", "\033[34m🏹\033[0m", 11, 0, 1),
            cls("Arc", "\033[34m🏹\033[0m", 14, 0, 1),
            cls("Arc", "\033[34m🏹\033[0m", 19, 0, 1),
            cls("Arc", "\033[34m🏹\033[0m", 26, 0, 1),
            cls("Massue", "\033[37m🔨\033[0m", 5, 0, 3),
            cls("Massue", "\033[37m🔨\033[0m", 22, 0, 3),
            cls("Massue", "\033[37m🔨\033[0m", 38, 0, 3),
            cls("Epée", "\033[37m⚔️\033[0m", 42, 0, 5),
            cls("Epée", "\033[37m⚔️\033[0m️", 53, 0, 5),
            cls("Eclair", "\033[33m⚡️\033[0m️️", 1, 0, 2),
            cls("Eclair", "\033[33m⚡️\033[0m️️", 4, 0, 2),
            cls("Eclair", "\033[33m⚡️\033[0m️️", 8, 0, 2),
            cls("Eclair", "\033[33m⚡️\033[0m", 17, 0, 2),
            cls("Eclair", "\033[33m⚡️\033[0m", 23, 0, 2),
            cls("Boules de feu", "\033[37m💥\033[0m", 48, 0, 7),
            cls("Boules de feu", "\033[37m💥\033[0m", 49, 0, 7),
            cls("Potion  de vie mineures", "\033[31m❤\033[0m️️️️", 7, 1, 0),
            cls("Potion  de vie mineures", "\033[31m❤\033[0m️️️️", 13, 1, 0),
            cls("Potion  de vie mineures", "\033[31m❤\033[0m️️️️", 28, 1, 0),
            cls("Potion  de vie mineures", "\033[31m❤\033[0m", 29, 1, 0),
            cls("Potion  de vie mineures", "\033[31m❤\033[0m️️️️", 33, 1, 0),
            cls("Potion de vie standard", "\033[31m💕\033[0m️️️️", 31, 2, 0),
            cls("Potion de vie standard", "\033[31m💕\033[0m️️️", 39, 2, 0),
            cls("Potion de vie standard", "\033[31m💕\033[0m️️️️", 43, 2, 0),
            cls("Grande potion de vie", "\033[31m💖\033[0m", 41, 5, 0),
        ]
        return list_coffre

    def __repr__(self):
        return self.image
