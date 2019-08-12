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
                    plateau_de_jeu[i] = self.list_enemies[j].image_enemy
                j += 1
            while k < len(self.list_caisses_surprises):
                if i == self.list_caisses_surprises[k].case_surprise:
                    plateau_de_jeu[i] = self.list_caisses_surprises[k].image_surprise
                k += 1
            i += 1
        return plateau_de_jeu


class Enemy(object):

    def __init__(self, name_enemy, image_enemy, case_enemy, attack_points, life_points):
        self.name_enemy = name_enemy
        self.image_enemy = image_enemy
        self.case_enemy = case_enemy
        self.attack_points = attack_points
        self.life_points = life_points


class CaisseSurprise(object):

    def __init__(self, nom_surprise, image_surprise, case_surprise, ajout_pt_attack, ajout_pt_vie):
        self.nom_surprise = nom_surprise
        self.image_surprise = image_surprise
        self.case_surprise = case_surprise
        self.ajout_pt_attack = ajout_pt_attack
        self.ajout_pt_vie = ajout_pt_vie


