class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, nom, number_of_case, cases_dragons):
        self.nom = nom
        self.number_of_case = number_of_case
        self.cases_dragons = cases_dragons

    def get_name(self):
        """
        Returns
            str: The name of the map
        """
        return self.nom

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        return self.number_of_case

    def get_cases_dragons(self):
        return self.cases_dragons


class Ennemies(object):

    def __init__(self, name, image, cases):
        self.name = name
        self.image = image
        self.cases = cases

    def get_cases_ennemies(self):
        """
        une liste avec les cases où se cachent les ennemis
        :return:
        """
        return self.cases


