import os

# MAX_X = 1920
# MAX_Y = 1080
# FRAME_RATE = 30

# Lower resolution settings
MAX_X = 600
MAX_Y = 1000
FRAME_RATE = 10

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_CHARACTER1 = os.path.join(os.getcwd(), "")
IMAGE_HEALTH = os.path.join(os.getcwd(), "")
IMAGE_BIN = os.path.join(os.getcwd(), "")
IMAGE_PAPER = os.path.join(os.getcwd(), "")
IMAGE_GLASS = os.path.join(os.getcwd(), "")
IMAGE_METAL = os.path.join(os.getcwd(), "")

SOUND_START = os.path.join(os.getcwd(), "./assets/start.wav")
SOUND_SOUNDTRACK = os.path.join(os.getcwd(), "")
SOUND_PAPER_SORT = os.path.join(os.getcwd(), "")
SOUND_GLASS_SORT = os.path.join(os.getcwd(), "")
SOUND_METAL_SORT = os.path.join(os.getcwd(), "")
SOUND_OVER = os.path.join(os.getcwd(), "./assets/over.wav")

FALLING_SPEED = 1
RECYCLABLE_GENERATION_WAIT_TIME = 3  # seconds
RECYCLABLE_FRAME_COUNT = RECYCLABLE_GENERATION_WAIT_TIME * FRAME_RATE


PAPER_WIDTH = 20
PAPER_HEIGHT = 20

GLASS_WIDTH = 20
GLASS_HEIGHT = 20

METAL_WIDTH = 20
METAL_HEIGHT = 20


SCORE_WIDTH = 100
SCORE_HEIGHT = 20

HEALTH_WIDTH = MAX_X - SCORE_WIDTH
HEALTH_HEIGHT = 20
HEALTH_X = 0
HEALTH_Y = MAX_Y - HEALTH_HEIGHT

SCORE_X = HEALTH_X + HEALTH_WIDTH
SCORE_Y = HEALTH_Y


BIN_WIDTH = MAX_X // 3
BIN_HEIGHT = 100
PAPER_BIN_X = 0
GLASS_BIN_X = BIN_WIDTH
METAL_BIN_X = 2 * BIN_WIDTH
BIN_Y = MAX_Y - BIN_HEIGHT - HEALTH_HEIGHT
