from game.action import Action
from game import constants
from game.point import Point
from game.actors.paper import Paper
from game.actors.glass import Glass
from game.actors.metal import Metal
import random


class GenerateRecyclablesAction(Action):
    """A counter instigated function generates a random amount of recyclables and adds them to the cast list"""

    def __init__(self):
        """The class constructor.

        Args:
            cast (dictionary): An dictionary containing all actors.
        """
        super().__init__()

    def execute(self, cast):
        frame_counter = 0
        frame_counter += 1
        if frame_counter > constants.RECYCLABLE_FRAME_COUNT:
            frame_counter = 0
            for i in range(0, random.randint(0, 3)):
                recyclable_type = random.randint(1, 3)
                if recyclable_type == 1:
                    recyclable = Paper()
                    recyclable.set_velocity = Point(0, 1)
                elif recyclable_type == 2:
                    recyclable = Glass()
                    recyclable.set_velocity = Point(0, 1)
                elif recyclable_type == 3:
                    recyclable = Metal()
                    recyclable.set_velocity = Point(0, 1)
                # add recyclable to cast list (name is non-unique)
                cast["recyclables"].append(recyclable)
