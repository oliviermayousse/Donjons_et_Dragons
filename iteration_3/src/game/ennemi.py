from .base import BaseName, BaseCompetence


class Ennemi(BaseName, BaseCompetence):

    def __init__(self, name, image, case, life, attack_level):
        BaseName.__init__(self, name)
        BaseCompetence.__init__(self, image, life, attack_level)
        self.case = case

    @classmethod
    def get_list_ennemi(cls):
        list_ennemi = [
            cls("Dragon", "\033[32m🐉\033[0m", 45, 15, 4),
            cls("Dragon", "\033[32m🐉\033[0m", 52, 15, 4),
            cls("Dragon", "\033[32m🐉\033[0m", 56, 15, 4),
            cls("Dragon", "\033[32m🐉\033[0m", 62, 15, 4),
            cls("Sorciers", "\033[36m🌒\033[0m", 10, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 20, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 25, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 32, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 35, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 36, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 37, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 40, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 44, 9, 2),
            cls("Sorciers", "\033[36m🌒\033[0m", 47, 9, 2),
            cls("Gobelins", "\033[35m🧟\033[0m", 3, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 6, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 9, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 12, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 15, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 18, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 21, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 24, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 27, 6, 1),
            cls("Gobelins", "\033[35m🧟\033[0m", 30, 6, 1),
        ]
        return list_ennemi

    def __repr__(self):
        return self.image
