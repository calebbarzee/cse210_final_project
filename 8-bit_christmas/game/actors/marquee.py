from game.actor import Actor
from game import constants


class Marquee(Actor):
    def __init__(self):
        super().__init__(constants.MARQUEE_X, constants.MARQUEE_Y)

        self._description = ""
        self.set_width(constants.MARQUEE_WIDTH)
        self.set_height(constants.MARQUEE_HEIGHT)
