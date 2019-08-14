

class Personnage:
    """
    This interface contains all data needed by the client about the hero
    """

    def __init__(self, name, image, attack_level, life_points):
        self.name = name
        self.image = image
        self.attack_level = attack_level
        self.life_points = life_points

    def get_name(self):
        return self.name











