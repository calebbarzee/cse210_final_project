from game.actor import Actor
from game import constants


class MetalBin(Actor):
    """Bin type metal that sits at the bottom of the screen as a bin to collect metal."""

    def __init__(self):
        super().__init__(constants.METAL_BIN_X, constants.BIN_Y,
                         constants.BIN_WIDTH, constants.BIN_HEIGHT)
