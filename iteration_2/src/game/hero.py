class Hero(object):

    """
    This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, current_life_points, attaque):

        self.name = name
        self.image = image
        self.current_life_points = current_life_points
        self.attaque = attaque

    def get_name(self):
        """
        Returns
            str: the name of the hero
        """
        return self.name

    def get_image(self):
        """
        Returns
            str: the image of the hero
        """
        return

    def get_life(self):
        """
        Returns
            int: the life level of the hero
        """
        return self.current_life_points

    def get_attack_level(self):
        """
        Returns
            int: the attack level of the hero
        """
        return self.attaque


