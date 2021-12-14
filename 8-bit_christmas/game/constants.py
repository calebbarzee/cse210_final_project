import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
PRESENTS = 10

BACKGROUND_HEIGHT = MAX_Y
BACKGROUND_WIDTH = MAX_X
BACKGROUND_IMAGE = PATH + "/assets/images/christmas_landscape.png"

DEFAULT_BLOCK_SIZE = 15
DEFAULT_FONT_SIZE = 20

CHARACTER_HEIGHT = 30
CHARACTER_WIDTH = 20
CHARACTER_INITIAL_X = 580
CHARACTER_INITIAL_Y = 40
CHARACTER_SPEED = 4
CHARACTER_IMAGE = PATH + "/assets/images/christmas_landscape.png"


# MARQUEE_HEIGHT = 30
# MARQUEE_WIDTH = 300
MARQUEE_X = 0
MARQUEE_Y = MAX_Y - 30
