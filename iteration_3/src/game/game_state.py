from random import randint
from .hero import Hero
from .caissesurprise import CaisseSurprise
from .enemy import Enemy
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

    def lancer_le_de(self):
        dice = randint(1, 6)
        return dice


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

        dice = self.lancer_le_de()
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
        #ajout des infos sur la case courrante
        self.log.append("voici ce que le héro a trouvé sur la case:")

        #si le héro n'est toujours pas sorti du plateau de jeu
        if self.current_case < self.map.number_of_case:
            # appel de la fonction qui permet de savoir ce qu'il y a dans la case et ajout dans le log
            self.log.append(self.hero.verif_ce_qu_il_y_a_dans_current_case(plateau_de_jeu[self.current_case]))
            # si le contenu est de Class CaisseSurpires
            # appel fonction qui vérifie si le héro peut récupérer les points de la caisse surprise
            if isinstance(plateau_de_jeu[self.current_case], CaisseSurprise):
                self.log.append(self.hero.ramassage_objet(plateau_de_jeu[self.current_case]))
            #si le contenu est de Class Enemy,
            if isinstance(plateau_de_jeu[self.current_case], Enemy):
                #affichage des caractéristiques de l'enemy rencontré
                self.log.append("il a %s point de vie" %plateau_de_jeu[self.current_case].life_points)
                self.log.append("son niveau d'attaque est de %s point" %plateau_de_jeu[self.current_case].attack_level)
                #appel de la fonction Combat
                nouveau_point_vie_hero = self.hero.combat(plateau_de_jeu[self.current_case])
                #vérifier si le héro est mort ou non
                if nouveau_point_vie_hero == 0:
                    print("\n".join(self.log))
                    print("le héro est mort!!! GAME OVER")
                    self.current_case = self.map.number_of_case + 1
                else:
                    self.log.append("le héro est ressorti vainqueur du combat")
                    if plateau_de_jeu[self.current_case].life_points > 0:
                        self.log.append("point de vie de l'enemy après combat : %s" %plateau_de_jeu[self.current_case].life_points)
                    else:
                        self.log.append("l'enemy est mort")
                    self.log.append("nouveau point de vie du héro : %s" %self.hero.life_points)
        # à l'inverse, si le héro sort du plateau
        else:
            print("\n".join(self.log))
            print("le héro est arrivé au bout du plateau GAGNE!")

        #ajout dans le log d'une ligne de séparation pour y voir plus clair dans la console
        self.log.append("\033[33m===========================NEXT TURN========================================\033[0m")

        return self.log