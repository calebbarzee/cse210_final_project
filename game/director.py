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
from game.actors.paper import Paper
from game.actors.glass import Glass
from game.actors.metal import Metal
from game.bins.paper_bin import Paper_Bin
from game.bins.glass_bin import Glass_Bin
from game.bins.metal_bin import Metal_Bin
from game.services.object_state import Object_State


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
            cast (list): The game actors (objects).
            script (list): The game actions (objects).
            keep_playing: game control variable.
        """
        self._cast = []
        self._script = []
        self._keep_playing = True
        self._input_service = InputService()
        self._output_service = OutputService()
        self._audio_service = AudioService()
        
        self._score = Score()
        self._health = Health()
        # placeholder comment for character actor
        self._paper_bin = Paper_Bin()
        self._glass_bin = Glass_Bin()
        self._metal_bin = Metal_Bin()
        self._cast.append(self._score)
        self._cast.append(self._health)
        # placeholder comment for character actor
        self._cast.append(self._paper_bin)
        self._cast.append(self._glass_bin)
        self._cast.append(self._metal_bin)

        self._object_state = Object_State()
        self._frame_counter = 0


    def open_window(self):
        # Start the game
        self._output_service.open_window("Save The Earth")
        self._audio_service.start_audio()
        # audio_service.play_sound(constants.SOUND_START)


    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        """Generates and runs the list of methods in script based on actors present in cast."""
        while self._keep_playing:
            # input services (mainly a place holder for future expansion of menu pages)
            # (state machine for game input contained within object_state)

            # updates of actor attributes (score, health, recyclables velocity) and clearing of old falling_objects.
            self._frame_counter += 1
            if self._frame_counter > constants.RECYCLABLE_FRAME_COUNT:
                self._frame_counter = 0
                self.generate_recyclables()
            self.evaluate_recyclables_state()

            # output of actors on screen
            self._output_service.clear_screen()
            self._output_service.draw_actors(self._cast)
            self._output_service.flush_buffer()

            if raylibpy.window_should_close():
                self._keep_playing = False
                self._audio_service.stop_audio()


    def generate_recyclables(self):
        """A counter instigated function generates a random amount of recyclables and adds them to the cast list"""
        for i in range(0, random.randint(0, 3)):
            recyclable_type = random.randint(1, 3)
            if recyclable_type == 1:
                recyclable = Paper()
            elif recyclable_type == 2:
                recyclable = Glass()
            elif recyclable_type == 3:
                recyclable = Metal()
            # add recyclable to cast list (name is non-unique)
            self._cast.append(recyclable)


    def evaluate_recyclables_state(self):
        for actor in self._cast:
            if actor._type == "recyclable":
                self._object_state.drag_state(actor)
                self._object_state.clear_recyclable(
                    actor, self._cast, self._health, self._score)
