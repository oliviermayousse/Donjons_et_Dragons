

class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, name, number_of_case, ennemies, objet):

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


class Ennemie(object):
    def __init__(self, name, image, cases, pdv, degats):
        self.name = name
        self.image = image
        self.cases = cases
        self.pdv = pdv
        self.degats = degats

    def __repr__(self):
        return self.image

    def get_case_ennemie(self):
        return self.cases


class Objet(object):
    def __init__(self, name, image, cases, pdv, degats):
        self.name = name
        self.image = image
        self.cases = cases
        self.pdv = pdv
        self.degats = degats

    def __repr__(self):
        return self.image

    def get_cases_objet(self):
        return self.cases



