from game.actor import Actor
from game import constants


class Glass_Bin(Actor):
    """Bin type glass that sits at the bottom of the screen as a bin to collect glass."""

    def __init__(self):
        super().__init__(300, 800, constants.GLASS_BIN_WIDTH, constants.GLASS_BIN_HEIGHT)
