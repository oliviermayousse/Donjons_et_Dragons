class Coffre(object):

    def __init__(self, name, image, case, life, attack_level):
        self.name = name
        self.image = image
        self.case = case
        self.life = life
        self.attack_level = attack_level

    @classmethod
    def get_list_coffre(cls):
        list_coffre = [
            cls("Arc", "🏹", 2, 0, 1),
            cls("Arc", "🏹", 11, 0, 1),
            cls("Arc", "🏹", 14, 0, 1),
            cls("Arc", "🏹", 19, 0, 1),
            cls("Arc", "🏹", 26, 0, 1),
            cls("Massue", "🔨", 5, 0, 3),
            cls("Massue", "🔨", 22, 0, 3),
            cls("Massue", "🔨", 38, 0, 3),
            cls("Epée", "⚔️", 42, 0, 5),
            cls("Epée", "⚔️", 53, 0, 5),
            cls("Eclair", "⚡️️", 1, 0, 2),
            cls("Eclair", "⚡️️", 4, 0, 2),
            cls("Eclair", "⚡️️", 8, 0, 2),
            cls("Eclair", "⚡️️", 17, 0, 2),
            cls("Eclair", "⚡️️", 23, 0, 2),
            cls("Boules de feu", "💥️️️", 48, 0, 7),
            cls("Boules de feu", "💥️️️", 49, 0, 7),
            cls("Potion  de vie mineures", "❤️️️️", 7, 1, 0),
            cls("Potion  de vie mineures", "❤️️️️", 13, 1, 0),
            cls("Potion  de vie mineures", "❤️️️️", 28, 1, 0),
            cls("Potion  de vie mineures", "❤️️️️", 29, 1, 0),
            cls("Potion  de vie mineures", "❤️️️️", 33, 1, 0),
            cls("Potion de vie standard", "💕️️️️", 31, 2, 0),
            cls("Potion de vie standard", "💕️️️️", 39, 2, 0),
            cls("Potion de vie standard", "💕️️️️", 43, 2, 0),
            cls("Grande potion de vie", "💖", 41, 5, 0),
        ]
        return list_coffre

    def __repr__(self):
        return self.image
