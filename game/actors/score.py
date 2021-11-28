from game.actor import Actor
from game import constants


class Score(Actor):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        score: an integer representing points accumulated by user
    """

    def __init__(self):
        super().__init__(200, 200, 100, 20)
        self._score = 0

    def update_score(self, points):
        self._score += points
