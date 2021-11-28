import os

# MAX_X = 1920
# MAX_Y = 1080
# FRAME_RATE = 30

# Lower resolution settings
MAX_X = 600
MAX_Y = 1200
FRAME_RATE = 30

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
RECYCLABLE_GENERATION_WAIT_TIME = 3

PAPER_WIDTH = 100
PAPER_HEIGHT = 100

GLASS_WIDTH = 100
GLASS_HEIGHT = 100

METAL_WIDTH = 100
METAL_HEIGHT = 100

HEALTH_WIDTH = 1000
HEALTH_HEIGHT = 100

PAPER_BIN_WIDTH = 300
GLASS_BIN_WIDTH = 300
METAL_BIN_WIDTH = 300
