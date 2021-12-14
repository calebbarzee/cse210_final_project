import random
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        marquee = cast["marquee"][0]  # there's only one
        character = cast["character"][0]  # there's only one
        presents = cast["presents"]
        marquee.set_text("")
        for present in presents:
            if self._physics_service.is_collision(character, present):
                description = present.get_description()
                marquee.set_text(description)
