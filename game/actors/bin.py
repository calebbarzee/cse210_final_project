from game.actor import Actor


class Bin(Actor):
    """Class of actors that sit at the bottom of the screen as bins to collect recyclables."""

    def __init__(self):
        super().__init__()
