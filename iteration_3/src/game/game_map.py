from .base import BaseName


class Map(BaseName):
    """
    This interface contains all data needed by the client about the game map
    """
    def __init__(self, name, number_of_case, liste_ennemis, liste_coffres):
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
            plateau[coffre.case] = coffre

        return plateau









