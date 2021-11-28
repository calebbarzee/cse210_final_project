from game import constants
from game.director import Director


def main():

    # Start the game
    output_service.open_window("Save The Earth")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director()
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
