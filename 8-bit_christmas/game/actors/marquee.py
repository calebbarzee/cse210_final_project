from game.actor import Actor
from game import constants


class Marquee(Actor):
    def __init__(self):
        super().__init__(constants.MARQUEE_X, constants.MARQUEE_Y)

        self._description = ""
