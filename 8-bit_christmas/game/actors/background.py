from game.actor import Actor
from game import constants


class Background(Actor):
    def __init__(self):
        super().__init__(0, 0)

        self._description = ""
        self.set_width(constants.BACKGROUND_WIDTH)
        self.set_height(constants.BACKGROUND_HEIGHT)
        self.set_image(constants.BACKGROUND_IMAGE)
