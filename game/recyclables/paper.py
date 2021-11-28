from game.actors.falling_obj import Falling_Obj
from game import constants


class Paper(Falling_Obj):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
        _width (int): The actor's width
        _height (int): The actor's height
        _image (string): The file path of the image file (if present)
    """

    def __init__(self):
        super().__init__()
        self.set_image = constants.IMAGE_PAPER
