from typing import cast
from game.action import Action
from game.services.output_service import OutputService


class DrawActorsAction(Action):
    def __init__(self, output_service):
        super().__init__()
        self.output_service = output_service

    def execute(self, cast):
        self.output_service.clear_screen()
        for actor in cast["marquee"]:
            self.output_service.draw_actor(actor)
        for actor in cast["character"]:
            self.output_service.draw_actor(actor)
        for actor in cast["artifact"]:
            self.output_service.draw_actor(actor)
        self.output_service.flush_buffer()
