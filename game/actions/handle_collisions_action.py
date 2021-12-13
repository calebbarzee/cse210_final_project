import random
from game import constants
from game.action import Action
from game.point import Point


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
        # ball = cast["balls"][0]  # there's only one
        # paddle = cast["paddle"][0]  # there's only one
        # bricks = cast["bricks"]
        # if self._physics_service.is_collision(ball, paddle):
        #     ball_velocity_y = ball.get_velocity().get_y()
        #     ball_velocity_y *= -1
        #     ball_velocity_x = ball.get_velocity().get_x()
        #     ball.set_velocity(Point(ball_velocity_x, ball_velocity_y))
        # for brick in bricks:
        #     if self._physics_service.is_collision(ball, brick):
        #         ball_velocity_y = ball.get_velocity().get_x()
        #         ball_velocity_y *= -1
        #         ball_velocity_x = ball.get_velocity().get_x()
        #         ball.set_velocity(Point(ball_velocity_x, ball_velocity_y))
        #         index = bricks.index(brick)
        #         cast["bricks"].pop(index)
