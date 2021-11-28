from game.falling_obj import Falling_Obj
from game import constants


class Glass(Falling_Obj):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:


    Attributes:

    """

    def __init__(self):
        super().__init__()
        self.set_image = constants.IMAGE_GLASS
