
class Hero(object):
    """
    This interface contains all data needed by the client about the hero
    """
    def __init__(self, name, image, life, attack_level):
        self.name = name
        self.image = image
        self.life = life
        self.attack_level = attack_level

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


# class Warrior(Hero):
#     name = "Warrior"
#     life = 5
#     attack_level = random.randrange(5, 10)
#
#
# class Wizard(Hero):
#     name = "Wizard"
#     life = random.randrange(3, 6)
#     attack_level = random.randrange(8, 15)
