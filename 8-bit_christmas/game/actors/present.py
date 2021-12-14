from game.actor import Actor
from game import constants
import random


class Present(Actor):
    """
    Defines an artifact in the game. Inherits from Actor, and adds a description.
    """

    def __init__(self):
        super().__init__(random.randint(100, constants.MAX_X - 100),
                         random.randint(450, constants.MAX_Y - 50))

        self._description = ""
        self.set_width(constants.PRESENT_WIDTH)
        self.set_height(constants.PRESENT_HEIGHT)
        self.set_image(constants.PRESENT_IMAGE)

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def has_description(self):
        """
        Returns true if the description is not "".
        """
        return self._description != ""
