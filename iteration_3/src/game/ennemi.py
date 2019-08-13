class Ennemi(object):

    def __init__(self, name, image, case, life, attack_level):
        self.name = name
        self.image = image
        self.case = case
        self.life = life
        self.attack_level = attack_level

    @classmethod
    def get_list_ennemi(cls):
        list_ennemi = [
            cls("Dragon", "🐉", 45, 15, 4),
            cls("Dragon", "🐉", 52, 15, 4),
            cls("Dragon", "🐉", 56, 15, 4),
            cls("Dragon", "🐉", 62, 15, 4),
            cls("Sorciers", "🌒", 10, 9, 2),
            cls("Sorciers", "🌒", 20, 9, 2),
            cls("Sorciers", "🌒", 25, 9, 2),
            cls("Sorciers", "🌒", 32, 9, 2),
            cls("Sorciers", "🌒", 35, 9, 2),
            cls("Sorciers", "🌒", 36, 9, 2),
            cls("Sorciers", "🌒", 37, 9, 2),
            cls("Sorciers", "🌒", 40, 9, 2),
            cls("Sorciers", "🌒", 44, 9, 2),
            cls("Sorciers", "🌒", 47, 9, 2),
            cls("Gobelins", "🧟", 3, 6, 1),
            cls("Gobelins", "🧟", 6, 6, 1),
            cls("Gobelins", "🧟", 9, 6, 1),
            cls("Gobelins", "🧟", 12, 6, 1),
            cls("Gobelins", "🧟", 15, 6, 1),
            cls("Gobelins", "🧟", 18, 6, 1),
            cls("Gobelins", "🧟", 21, 6, 1),
            cls("Gobelins", "🧟", 24, 6, 1),
            cls("Gobelins", "🧟", 27, 6, 1),
            cls("Gobelins", "🧟", 30, 6, 1),
        ]
        return list_ennemi

    def __repr__(self):
        return self.image
