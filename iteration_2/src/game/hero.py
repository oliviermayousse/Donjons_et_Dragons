class Hero(object):
    """
    This interface contains all data needed by the client about the hero
    """

    def __init__(self, nom, image, life, attack_level):
        self.nom = nom
        self.image = image
        self.life = life
        self.attack_level = attack_level

    def get_name(self):
        """
        Returns
            str: the name of the hero
        """
        return self.nom


    def get_image(self):
        """
        Returns
            str: the image of the hero
        """
        return self.image

    def get_life(self):
        """
        Returns
            int: the life level of the hero
        """
        return self.life

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attack_level
