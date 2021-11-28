from game.actors.falling_obj import Falling_Obj
from game import constants


class Metal(Falling_Obj):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:


    Attributes:
        recyclable_type: type of recyclable (paper, glass, or metal) 
    """

    def __init__(self):
        super().__init__()
        self._recyclable_type = "metal"
        self.set_image = constants.IMAGE_METAL
