class BaseName:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Returns
            str: the name of the hero
        """
        return self.name


class BaseCompetence:

    def __init__(self, image, life, attack_level):
        self.image = image
        self.life = life
        self.attack_level = attack_level

    def get_image(self):
        """
        Returns
            str: the image of the hero
        """
        return self.image

