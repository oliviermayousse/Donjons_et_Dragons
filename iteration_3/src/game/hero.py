from .caissesurprise import CaisseSurprise
from .enemy import Enemy

class Hero(object):
    """
    This interface contains all data needed by the client about the hero
    """

    def __init__(self, name, image, life_points, attack_level, max_life_points, max_attack_level):
        self.name = name
        self.image = image
        self._life_points = life_points
        self._attack_level = attack_level
        self.max_life_points = max_life_points
        self.max_attack_level = max_attack_level

    def get_name(self):
        return self.name

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
    def life_points(self):
        return self._life_points

    @life_points.setter
    def life_points(self, life_points):
        if life_points >= self.max_life_points:
            self._life_points = self.max_life_points
        else:
            self._life_points = life_points

    def verif_ce_qu_il_y_a_dans_current_case(self, contenu_case_courante):
        if isinstance(contenu_case_courante, Enemy) or isinstance(contenu_case_courante, CaisseSurprise):
            return contenu_case_courante.get_name()
        else:
            return "la case est vide"

    # fonction qui permet de vérifier sur le héro peut ou non récupérer les points de la caisse surprise
    def ramassage_objet(self, caisse_surprise):
        if caisse_surprise.nom_surprise == "Potion de vie mineure" or caisse_surprise.nom_surprise == "grande potion de vie" or caisse_surprise.nom_surprise == "Potion de vie standard":
            point_de_vie_bonus = caisse_surprise.ajout_pt_vie
            self.life_points += point_de_vie_bonus
            return("nouveau point de vie du héro :%s" %self.life_points)
        elif self.name == "Guerrier":
            if caisse_surprise.nom_surprise == "Arc" or caisse_surprise.nom_surprise == "Massue" or caisse_surprise.nom_surprise =="Epée":
                point_attack_bonus = caisse_surprise.ajout_pt_attack
                self.attack_level += point_attack_bonus
                return("nouveau Attack Level du héro :%s" % self.attack_level)
            else:
                return("notre héro ne peut pas ramaser cet objet...dommage...")
        elif self.name == "Magicien":
            if caisse_surprise.nom_surprise == "Eclair" or caisse_surprise.nom_surprise == "Boule de feu":
                point_attack_bonus = caisse_surprise.ajout_pt_attack
                self.attack_level = point_attack_bonus
                return("nouveau Attack Level du héro :%s" % self.attack_level)
            else:
                return("notre héro ne peut pas ramaser cet objet...dommage...")


    def combat(self, enemy):
        #le héro commence par attaquer
        enemy.life_points -= self._attack_level
        #si l'enemy n'est pas mort, il réplique
        if enemy.life_points > 0:
            self._life_points -= enemy.attack_points
        return self._life_points








