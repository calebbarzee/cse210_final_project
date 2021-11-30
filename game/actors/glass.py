import random
from game.point import Point
from game.actor import Actor
from game import constants


class Glass(Actor):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:


    Attributes:
        recyclable_type: type of recyclable (paper, glass, or metal) 
    """

    def __init__(self):
        x = random.randint(100, constants.MAX_X - 100)
        super().__init__(x, 0,
                         constants.GLASS_WIDTH, constants.GLASS_HEIGHT)
        # ^^^ initializes the object at the top of the screen 100 units from the edges of the screen
        # ^^^ last two arguments set the width and height of the actor
        self.set_velocity(Point(0, 1))
        self._type = "recyclable"
        self._recyclable_type = "glass"
        self.set_image = constants.IMAGE_GLASS
