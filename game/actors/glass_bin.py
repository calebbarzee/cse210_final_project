from game.actor import Actor
from game import constants


class GlassBin(Actor):
    """Bin type glass that sits at the bottom of the screen as a bin to collect glass."""

    def __init__(self):
        super().__init__(constants.GLASS_BIN_X, constants.BIN_Y,
                         constants.BIN_WIDTH, constants.BIN_HEIGHT)
