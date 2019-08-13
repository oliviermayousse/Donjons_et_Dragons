from .Objet import Objet

from .game_state import *


class Hero(object):

    """
    This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, current_life_points, max_life_points,attaque, max_attaque):

        self.name = name
        self.image = image
        self.current_life_points = current_life_points
        self.max_life_points = max_life_points
        self.attaque = attaque
        self.max_attaque = max_attaque

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

    def get_life(self):
        """
        Returns
            int: the life level of the hero
        """
        return self.current_life_points

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attaque

    @classmethod
    def get_heroes(cls):
        guerrier = cls(name="Guerrier", image="🤺", current_life_points="5", max_life_points="10", attaque="5", max_attaque="10")
        magicien = cls(name="Magicien", image="🧙 ", current_life_points="3", max_life_points="6", attaque="8", max_attaque="15")
        heroes_list = [guerrier, magicien]
        return heroes_list

    def condition_equipement(self, objet):
        if self.name == "Magicien":
            if objet.name == "Sort éclair" or objet.name == "Sort Boule de feu" or objet.name == "Petite potion" or objet.name == "Potion standards" or objet.name == "Grand potion":
                return True
            else:
                return False
        else:
            if objet.name == "Sort éclair" or objet.name == "Sort Boule de feu":
                return False
            elif objet.name == "Petite potion" or objet.name == "Potion standards" or objet.name == "Grand potion":
                return True
            else:
                return True



