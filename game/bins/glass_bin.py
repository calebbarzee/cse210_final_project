from game.actor import Actor


class Glass_Bin(Actor):
    """Bin type glass that sits at the bottom of the screen as a bin to collect glass."""

    def __init__(self):
        super().__init__(300, 1000, 300, 200)
