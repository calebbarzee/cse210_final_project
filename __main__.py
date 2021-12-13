import os
# os.environ['RAYLIB_BIN_PATH'] = '.'
import random
import raylibpy
from game.director import Director
from game import constants
from game.actor import Actor
from game.point import Point
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.audio_service import AudioService
from game.services.physics_service import PhysicsService
from game.actors.score import Score
from game.actors.health import Health
from game.actors.paper_bin import PaperBin
from game.actors.glass_bin import GlassBin
from game.actors.metal_bin import MetalBin
from game.actions.handle_collisions_action import HandleCollisionsAction
from game.actions.move_actors_action import MoveActorsAction
from game.actions.draw_actors_action import DrawActorsAction
from game.actions.generate_recyclables_action import GenerateRecyclablesAction
from game.actions.drag_state_action import DragStateAction


def main():
    cast = []
    script = []
    keep_playing = True
    input_service = InputService()
    output_service = OutputService()
    audio_service = AudioService()

    score = Score()
    health = Health()
    # placeholder comment for character actor
    paper_bin = PaperBin()
    glass_bin = GlassBin()
    metal_bin = MetalBin()

    # object_state = ObjectState() make object state update action to handle click and drag

    # create the cast {key: tag, value: list}
    cast = {}

    cast["score"] = [score]
    cast["health"] = [health]
    cast["bins"] = [paper_bin, glass_bin, metal_bin]

    cast["recyclables"] = []

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    generate_recyclables_action = GenerateRecyclablesAction()
    drag_state_action = DragStateAction(input_service)

    script["input"] = [drag_state_action]
    script["update"] = [move_actors_action,
                        handle_collisions_action, generate_recyclables_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Save The Earth")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        """Generates and runs the list of methods in script based on actors present in cast."""
        while self._keep_playing:
            # input services (mainly a place holder for future expansion of menu pages)
            # (state machine for game input contained within object_state)

            # updates of actor attributes (score, health, recyclables velocity) and clearing of old falling_objects.

            self.evaluate_recyclables_state()

            if raylibpy.window_should_close():
                self._keep_playing = False

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
