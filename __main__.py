import os
os.environ['RAYLIB_BIN_PATH'] = '.'

from game import constants
from game.director import Director


def main():
    director = Director()
    director.open_window()
    director.start_game()


if __name__ == "__main__":
    main()
