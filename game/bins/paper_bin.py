from game.actor import Actor
from game import constants


class Paper_Bin(Actor):
    """Bin type paper that sits at the bottom of the screen as a bin to collect paper."""

    def __init__(self):
        super().__init__(constants.PAPER_BIN_X, constants.BIN_Y, constants.BIN_WIDTH, constants.BIN_HEIGHT)
