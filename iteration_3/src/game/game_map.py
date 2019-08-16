from .base import BaseName
from .ennemi import Ennemi
from .coffre import Coffre


class NotEmptyException(Exception):
    pass


class Map(BaseName):
    """
    This interface contains all data needed by the client about the game map
    """
    def __init__(self, name, number_of_case, liste_ennemis=None, liste_coffres=None):
        if liste_ennemis is None:
            liste_ennemis = []
        if liste_coffres is None:
            liste_coffres = []
        BaseName.__init__(self, name)
        self.number_of_case = number_of_case
        self.liste_ennemi = liste_ennemis
        self.liste_coffres = liste_coffres

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        return self.number_of_case

    def get_creat_map(self):

        plateau = []
        for i in range(0, self.number_of_case-1):
            plateau.append('.')
        for ennemi in self.liste_ennemi:
             plateau[ennemi.case] = ennemi
        for coffre in self.liste_coffres:
            if plateau[coffre.case] != ".":
                raise NotEmptyException()
            plateau[coffre.case] = coffre

        return plateau









