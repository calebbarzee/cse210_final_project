import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.input_service import InputService
from game.output_service import OutputService
from game.audio_service import AudioService


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    audio_service = AudioService()

    script["input"] = []
    script["update"] = []
    script["output"] = []

    # Start the game
    output_service.open_window("Save The Earth")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
