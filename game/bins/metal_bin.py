from game.actor import Actor


class Metal_Bin(Actor):
    """Bin type metal that sits at the bottom of the screen as a bin to collect metal."""

    def __init__(self):
        super().__init__(600, 1000, 300, 200)
