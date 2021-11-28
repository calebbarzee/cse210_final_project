from game.actor import Actor


class Paper_Bin(Actor):
    """Bin type paper that sits at the bottom of the screen as a bin to collect paper."""

    def __init__(self):
        super().__init__(0, 1000, 300, 200)
