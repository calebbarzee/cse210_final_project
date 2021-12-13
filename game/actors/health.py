from game.actor import Actor
from game import constants


class Health(Actor):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        health_score: an integer from 0-100
    """

    def __init__(self):
        super().__init__(constants.HEALTH_X, constants.HEALTH_Y,
                         constants.HEALTH_WIDTH, constants.HEALTH_HEIGHT)
        self.set_image = constants.IMAGE_HEALTH
        self.health_score = 100

    def update_health(self, value):
        # value is a negative integer of health lost from incorrect object sorting
        self.health_score += value
