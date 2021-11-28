import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.input_service import InputService
from game.output_service import OutputService
from game.audio_service import AudioService
from game.score import Score
from game.health import Health
from game.paper import Paper
from game.glass import Glass
from game.metal import Metal


def main():
    score = Score()
    health = Health()
    paper = Paper()
    glass = Glass()
    metal = Metal()
    # create the cast {key: tag, value: list}
    cast = {}
    cast["actors"] = [score, health, paper, glass, metal]

    input_service = InputService()
    output_service = OutputService()
    audio_service = AudioService()
    # Create the script {key: tag, value: list}
    # Ex.
    # script["input"] = []
    # script["update"] = []
    # script["output"] = []
    script = {}
    # place holder for mouse button state management
    # script["input"] = input_service.is_down_pressed

    # place holder for updating position of objects (possibly)
    # script["update"] = paper.set_velocity

    script["output"] = output_service.draw_actors

    # Start the game
    output_service.open_window("Save The Earth")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
