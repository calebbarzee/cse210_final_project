from game.actors.bin import Bin


class Paper_Bin(Bin):
    """Bin type paper that sits at the bottom of the screen as a bin to collect paper."""

    def __init__(self):
        super().__init__()
