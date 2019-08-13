from random import randint
from .hero import Hero
from .caissesurprise import CaisseSurprise
class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """

    def __init__(self, player_name, hero, map):
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.last_dice = None
        self.current_case = 0
        self.log = []

    def get_player_name(self):
        """
        Returns:
            str: The player name
        """
        return self.get_player_name()

    def get_game_id(self):
        """
        Returns:
            int: the game unique ID
        """
        return

    def get_game_status(self):
        """
        Returns:
            str: the game status
        """
        if self.current_case <= self.map.number_of_case:
            GAMESTATUS = "IN_PROGRESS"
        else:
            GAMESTATUS = "FINISHED"
        return GAMESTATUS

    def get_hero(self):
        """
        Returns:
            Hero: the current hero
        """

        return self.hero

    def get_map(self):
        """
        Returns:
            Map: the current map
        """
        return self.map

    def get_last_log(self):
        """
        Returns:
            str: the last log of the game. This log is displayed by the client after each game turn
        """
        last_log = "\n".join(map(str, self.log))
        return last_log

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return self.current_case

    @property
    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.
        """
        #initialisation du tableau de Log
        self.log = []

        #ajout dans le log du Nom Héro, point de vie, niveau d'attaque
        self.log.append("Nom du Héro : %s %s" % (self.hero.name, self.hero.image))
        self.log.append("Point de vie : %s" %self.hero.life_points)
        self.log.append("Point d'attaque : %s" %self.hero._attack_level)

        #lancer de Dé
        dice = randint(1, 6)
        self.last_dice = dice
        #le personnage avance sur la case suivante en fct du lancé de Dé
        self.current_case += dice
        #ajout dans le log du résultat du lancer de Dé
        self.log.append("résultat jet de dé : %s" %dice)

        #appel de la fonction create_map pour récupérer le plateau de jeu avec les ennemis et les caisses déjà positionnés dessous
        plateau_de_jeu = self.map.create_map()

        #création d'un plateau casté en string pour l'affichage
        plateau_de_presentation = list(map(str, plateau_de_jeu))
        i = 0
        while i <= (self.map.number_of_case - 1):
            if i == self.current_case:
                # àla case courrante on ajoute le Hero pour affichage
                plateau_de_presentation[i] += (self.hero.image)
            i += 1
        # ajout dans le log du plateau de jeu avec le héro positionné sur la case courante
        self.log.append("|".join(plateau_de_presentation))
        print("voici ce que le héro a trouvé sur la case:")
        #apel de la fonction qui permet de savoir ce qu'il y a dans la case
        print(self.hero.verif_ce_qu_il_y_a_dans_current_case(plateau_de_jeu[self.current_case]))
        #si le contenu est de Class CaisseSurpires, appel fonction qui vérifie si le héro peut récupérer les points de la caisse surprise
        if isinstance(plateau_de_jeu[self.current_case], CaisseSurprise):
           self.hero.ramassage_objet(plateau_de_jeu[self.current_case])





        return self.log