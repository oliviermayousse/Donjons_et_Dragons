class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, name, number_of_case, list_enemies, list_caisses_surprises):
        self.name = name
        self.number_of_case = number_of_case
        self.list_enemies = list_enemies
        self.list_caisses_surprises = list_caisses_surprises

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

    def create_map(self):
        plateau_de_jeu = []
        i = 0
        while i <= (self.number_of_case - 1):
            plateau_de_jeu.append(" ")
            i += 1

        i = 0
        while i <= (self.number_of_case - 1):
            j = 0
            k = 0
            while j < len(self.list_enemies):
                if i == self.list_enemies[j].case_enemy:
                    plateau_de_jeu[i] = self.list_enemies[j]
                j += 1
            while k < len(self.list_caisses_surprises):
                if i == self.list_caisses_surprises[k].case_surprise:
                    plateau_de_jeu[i] = self.list_caisses_surprises[k]
                k += 1
            i += 1
        return plateau_de_jeu

