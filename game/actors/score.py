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
        super().__init__(constants.SCORE_X, constants.SCORE_Y,
                         constants.SCORE_WIDTH, constants.SCORE_HEIGHT)
        self._score = 0
        self.set_text(str(self._score))

    def update_score(self, points):
        self._score += points
        self.set_text(str(self._score))
