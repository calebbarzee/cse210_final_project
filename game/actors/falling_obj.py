from game.point import Point
from game.actor import Actor
from game.mouse_state import Mouse_State
from game import constants
import random


class Falling_Obj(Actor):
    """A falling object that falls from the top of the screen, awaits user input to be dragged, and is cleared off at the bottom of the screen.

    Stereotype:


    Attributes:

    """

    def __init__(self):
        super().__init__(random.randint(100, (constants.MAX_X - 100)), 0, 100, 100)
        # ^^^ initializes the object at the top of the screen 100 units from the edges of the screen
        # ^^^ last two arguments set the width and height of the actor
        self.set_velocity = Point(0, 1)

    def clear_object(self):
        """clears the object off of the screen if it's at the bottom"""

    def evaluate_state(self):
        """calls mouse_state to evaluate if object is being dragged"""
        Mouse_State.drag_state(self)
