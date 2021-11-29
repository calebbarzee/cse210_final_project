from game.actor import Actor
from game import constants


class Paper_Bin(Actor):
    """Bin type paper that sits at the bottom of the screen as a bin to collect paper."""

    def __init__(self):
        super().__init__(0, 800, constants.PAPER_BIN_WIDTH, constants.PAPER_BIN_HEIGHT)
