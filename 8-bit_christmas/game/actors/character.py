from game.actor import Actor
from game import constants


class Character(Actor):
    def __init__(self):
        super().__init__(constants.CHARACTER_INITIAL_X, constants.CHARACTER_INITIAL_Y)

        self._description = ""
        self.set_width(constants.CHARACTER_WIDTH)
        self.set_height(constants.CHARACTER_HEIGHT)
