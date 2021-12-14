import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

PATH = os.path.dirname(os.path.abspath(__file__))

MESSAGES = open(PATH + "/messages.txt").read().splitlines()

PRESENTS = 7
PRESENT_HEIGHT = 32
PRESENT_WIDTH = 32
PRESENT_IMAGE = PATH + "/assets/images/presents.png"

BACKGROUND_HEIGHT = MAX_Y
BACKGROUND_WIDTH = MAX_X
BACKGROUND_IMAGE = PATH + "/assets/images/christmas_landscape.png"

DEFAULT_FONT_SIZE = 30

CHARACTER_HEIGHT = 45
CHARACTER_WIDTH = 45
CHARACTER_INITIAL_X = 580
CHARACTER_INITIAL_Y = 40
CHARACTER_SPEED = 4
CHARACTER_IMAGE = PATH + "/assets/images/characters.png"


# MARQUEE_HEIGHT = 30
# MARQUEE_WIDTH = 300
MARQUEE_X = 0
MARQUEE_Y = MAX_Y - 30

SOUNDTRACK1 = PATH + "/assets/audio/soundtrack1.wav"
SOUNDTRACK2 = PATH + "/assets/audio/soundtrack2.wav"
SOUNDTRACK3 = PATH + "/assets/audio/soundtrack3.wav"
SOUNDTRACK4 = PATH + "/assets/audio/soundtrack4.wav"
SOUNDTRACK5 = PATH + "/assets/audio/soundtrack5.wav"
SOUNDTRACK6 = PATH + "/assets/audio/soundtrack6.wav"
SOUNDTRACK7 = PATH + "/assets/audio/soundtrack7.wav"
SOUNDTRACK8 = PATH + "/assets/audio/soundtrack8.wav"
SOUNDTRACK9 = PATH + "/assets/audio/soundtrack9.wav"
SOUNDTRACK10 = PATH + "/assets/audio/soundtrack10.wav"
SOUNDTRACK11 = PATH + "/assets/audio/soundtrack11.wav"
SOUNDTRACK12 = PATH + "/assets/audio/soundtrack12.wav"
SOUNDTRACK13 = PATH + "/assets/audio/soundtrack13.wav"
SOUNDTRACK14 = PATH + "/assets/audio/soundtrack14.wav"
SOUNDTRACK15 = PATH + "/assets/audio/soundtrack15.wav"
