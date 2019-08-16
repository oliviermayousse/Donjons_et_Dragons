from .base import BaseName, BaseCompetence


class Hero(BaseName, BaseCompetence):
    """
    This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, max_life_point, attack_level, max_attack_level):
        self._life = life
        self.max_life_point = max_life_point
        self.min_life_point = 0
        self._attack_level = attack_level
        self.max_attack_level = max_attack_level
        BaseName.__init__(self, name)
        BaseCompetence.__init__(self, image, life, attack_level)

    @staticmethod
    def list_hero():

        return [Hero("Warrior", '\033[34m💪\033[0m', 5, 10, 5, 10), Hero("Wizard", '\033[34m🧙\033[0m', 3, 6, 8, 15)]

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
    def life(self):

        return self._life

    @life.setter
    def life(self, life):
        if life >= self.max_life_point:
            self._life = min(life, self.max_life_point)
        elif life < self.min_life_point:
            self._life = max(life, self.min_life_point)
        else:
            self._life = life

    def equipement(self, coffre):
        if coffre.name == "Potion  de vie mineures" or coffre.name == "Potion de vie standard" or coffre.name == "Grande potion de vie":
            self.life += coffre.life
        elif self.name == "Warrior":
            if coffre.name == "Arc" or coffre.name == "Massue" or coffre.name == "Epée":
                self.attack_level += coffre.attack_level
        elif self.name == "Wizard":
            if coffre.name == "Eclair" or coffre.name == "Boules de feu":
                self.attack_level += coffre.attack_level

    def combat(self, ennemi):

        ennemi.life -= self.attack_level
        if ennemi.life > 0:
            self.life -= ennemi.attack_level



