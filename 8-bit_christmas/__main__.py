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
from game.actors.artifact import Artifact
from game.actors.character import Character
from game.actors.marquee import Marquee


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    marquee = Marquee()
    marquee.set_text("")
    cast["marquee"] = [marquee]

    character = Character()
    character.set_text("#")
    cast["character"] = [character]

    artifacts = []
    for n in range(constants.ARTIFACTS):
        text = chr(random.randint(33, 126))
        description = constants.MESSAGES[n]

        artifact = Artifact()
        artifact.set_description(description)
        artifact.set_text(text)
        artifacts.append(artifact)
    cast["artifact"] = artifacts

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    output_service.open_window("character Finds Kitten")
    director = Director(cast, script)
    director.start_game()


if __name__ == "__main__":
    main()
