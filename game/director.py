from time import sleep
import random
import raylibpy
from game import constants
from game.actor import Actor
from game.point import Point
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.audio_service import AudioService
from game.actors.score import Score
from game.actors.health import Health
from game.recyclables.paper import Paper
from game.recyclables.glass import Glass
from game.recyclables.metal import Metal
from game.actors.bin import Bin
from game.bins.paper_bin import Paper_Bin
from game.bins.glass_bin import Glass_Bin
from game.bins.glass_bin import Metal_Bin


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self):
        """The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = []
        self._script = []
        self._keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if raylibpy.window_should_close():
                self._keep_playing = False

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """
        for action in self._script[tag]:
            action.execute(self._cast)

    def initialize_actors(self, cast):

        score = Score()
        health = Health()

    def generate_recyclables(self, cast):
        for i in range(0, random.randint(0, 3)):
            recyclable_type = random.randint(1, 3)
            if recyclable_type == 1:
                recyclable = Paper()
            elif recyclable_type == 2:
                recyclable = Glass()
            elif recyclable_type == 3:
                recyclable = Metal()
            # add recyclable to cast list (name is non-unique)
            cast["actors"].append(recyclable)

    def evaluate_recyclables_state(self, cast):
        for recyclable in cast["actors"]:
            recyclable.evaluate_state()
