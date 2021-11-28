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
    # create the cast {key: tag, value: list}
    cast = {}
    cast["actors"] = [score, health, ]
    generate_recyclables(cast)

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
    script["input"] = [input_service.]

    # place holder for updating position of objects (possibly)
    script["update"] = [evaluate_recyclables_state(), ]

    script["output"] = [output_service.draw_actors()]

    # Start the game
    output_service.open_window("Save The Earth")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


def generate_recyclables(cast):
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


def evaluate_recyclables_state(cast):
    for recyclable in cast["actors"]:
        recyclable.evaluate_state()


if __name__ == "__main__":
    main()
