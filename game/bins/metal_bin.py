from game.actor import Actor
from game import constants


class Metal_Bin(Actor):
    """Bin type metal that sits at the bottom of the screen as a bin to collect metal."""

    def __init__(self):
        super().__init__(600, 800, constants.METAL_BIN_WIDTH, constants.METAL_BIN_HEIGHT)
