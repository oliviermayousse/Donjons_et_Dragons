from .ennemi import Ennemi
from .coffre import Coffre

class Hero(object):
    """
    This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, max_life_point, attack_level, max_attack_level):
        self.name = name
        self.image = image
        self._life = life
        self.max_lif_point = max_life_point
        self._attack_level = attack_level
        self.max_attack_level = max_attack_level

    def get_name(self):
        """
        Returns
            str: the name of the hero
        """
        return self.name

    def get_image(self):
        """
        Returns
            str: the image of the hero
        """
        return self.image

    # def get_life(self):
    #     """
    #     Returns
    #         int: the life level of the hero
    #     """
    #     return self.life

    # def get_attack_level(self):
    #     """
    #     Returns
    #         int: the attack level of the hero
    #     """
    #     return self.attack_level

    @staticmethod
    def list_hero():

        return [Hero("Warrior", '💪', 5, 10, 5, 10), Hero("Wizard",'🧙', 3, 6, 8, 15)]

    @property
    def attack_level(self):

        return self._attack_level

    @attack_level.setter
    def attack_level(self, attack_level):
        if attack_level >= self.max_attack_level:
            self._attack_level = self.max_attack_level
        else:
            self._attack_level = attack_level

    @property
    def life(self):

        return self._life

    @life.setter
    def life(self, life):
        if life >= self.max_lif_point:
            self._life = self.max_lif_point
        else:
            self._life = life

    def equipement(self, coffre):
        if self.name == "Warrior":
            if coffre.name == "Arc" or coffre.name == "Massue" or coffre.name == "Epée":
                self.attack_level += coffre.attack_level
            else:
                self.life += coffre.life
        elif self.name == "Wizard":
            if coffre.name == "Eclair" or coffre.name == "Boules de feu":
                self.attack_level += coffre.attack_level
            else:
                self.life += coffre.life

    def combat(self, ennemi):

        ennemi.life -= self.attack_level
        if ennemi.life > 0:
            self.life -= ennemi.attack_level



