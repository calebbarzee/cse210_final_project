import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.actions.control_actors_action import ControlActorsAction
from game.actions.draw_actors_action import DrawActorsAction
from game.actions.handle_collisions_action import HandleCollisionsAction
from game.actions.move_actors_action import MoveActorsAction
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.physics_service import PhysicsService
from game.services.audio_service import AudioService
from game.actors.present import Present
from game.actors.character import Character
from game.actors.marquee import Marquee
from game.actors.background import Background


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    background = Background()
    cast["background"] = [background]

    marquee = Marquee()
    marquee.set_text("")
    cast["marquee"] = [marquee]

    character = Character()
    character.set_text("#")
    cast["character"] = [character]

    presents = []
    for n in range(constants.PRESENTS):
        description = constants.MESSAGES[n]

        present = Present()
        present.set_description(description)
        presents.append(present)
    cast["presents"] = presents

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    audio_service.start_audio()
    track = random.randint(1, 15)
    if track == 1:
        audio_service.play_sound(constants.SOUNDTRACK1)
    if track == 2:
        audio_service.play_sound(constants.SOUNDTRACK2)
    if track == 3:
        audio_service.play_sound(constants.SOUNDTRACK3)
    if track == 4:
        audio_service.play_sound(constants.SOUNDTRACK4)
    if track == 5:
        audio_service.play_sound(constants.SOUNDTRACK5)
    if track == 6:
        audio_service.play_sound(constants.SOUNDTRACK6)
    if track == 7:
        audio_service.play_sound(constants.SOUNDTRACK7)
    if track == 8:
        audio_service.play_sound(constants.SOUNDTRACK8)
    if track == 9:
        audio_service.play_sound(constants.SOUNDTRACK9)
    if track == 10:
        audio_service.play_sound(constants.SOUNDTRACK10)
    if track == 11:
        audio_service.play_sound(constants.SOUNDTRACK11)
    if track == 12:
        audio_service.play_sound(constants.SOUNDTRACK12)
    if track == 13:
        audio_service.play_sound(constants.SOUNDTRACK13)
    if track == 14:
        audio_service.play_sound(constants.SOUNDTRACK14)
    if track == 15:
        audio_service.play_sound(constants.SOUNDTRACK15)

    output_service.open_window("8-Bit Christmas Simulator")
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
