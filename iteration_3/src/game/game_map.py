from .objet import *
from .ennemie import *


class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, name, number_of_case, ennemies=None, objet=None):
        if ennemies is None:
            ennemies = []
        if objet is None:
            objet = []
        self.name = name
        self.number_of_case = number_of_case
        self.ennemies = ennemies
        self.objet = objet

    def get_name(self):
        """
        Returns
            str: The name of the map
        """

        return self.name

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        return self.number_of_case

    def get_map_list(self):

        plateau = []

        for i in range(1, self.number_of_case):

            plateau.append("_")

        for ennemie in self.ennemies:
            plateau[ennemie.cases] = ennemie

        for item in self.objet:
            plateau[item.cases] = item
        return plateau

    @classmethod
    def get_carte(cls):
        foret = cls(name="Forêt", number_of_case=64, ennemies=Ennemie.get_list_ennemie(), objet=Objet.get_objet_list())
        chateau = cls(name="Chateau", number_of_case=64, ennemies=Ennemie.get_list_ennemie(), objet=Objet.get_objet_list())
        list_map = [foret, chateau]
        return list_map







