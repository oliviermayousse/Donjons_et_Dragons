

class CaisseSurprise(object):

    def __init__(self, name, image_surprise, case_surprise, ajout_pt_attack, ajout_pt_vie):
        self.nom_surprise = name
        self.image_surprise = image_surprise
        self.case_surprise = case_surprise
        self.ajout_pt_attack = ajout_pt_attack
        self.ajout_pt_vie = ajout_pt_vie

    def get_name(self):
        return self.nom_surprise

    @classmethod
    def get_list_caisses_surprises(cls):
        return [cls("Arc", "\033[32m🏹\033[0m", 3, ajout_pt_attack=1, ajout_pt_vie=0),
                cls("Potion de vie mineure", "\033[32m🍾\033[0m", 7, ajout_pt_attack=0, ajout_pt_vie=1),
                cls("Boule de feu", "\033[32m🔥\033[0m", 8, ajout_pt_attack=7, ajout_pt_vie=0),
                cls("Boule de feu", "\033[32m🔥\033[0m", 6, ajout_pt_attack=7, ajout_pt_vie=0),
                cls("grande potion de vie", "\033[32m🍾\033[0m", 11,ajout_pt_attack= 0, ajout_pt_vie=5),
                cls("Boule de feu", "\033[32m🔥\033[0m", 9, ajout_pt_attack=7, ajout_pt_vie=0),
                cls("Eclair", "\033[32m🌩️\033[0m", 13, ajout_pt_attack=2, ajout_pt_vie=0),
                cls("Potion de vie standard", "\033[32m🍾\033[0m", 15, ajout_pt_attack=0, ajout_pt_vie=2),
                cls("Massue", "\033[32m🔨\033[0m", 8, ajout_pt_attack=3, ajout_pt_vie=0),
                cls("Epée", "\033[32m⚔\033[0m", 10, ajout_pt_attack=5, ajout_pt_vie=0)]

    def __repr__(self):
        return self.image_surprise