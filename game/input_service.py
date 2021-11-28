import sys
from game.point import Point
import raylibpy


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (InputService): An instance of InputService.
        """
        pass

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1

        if self.is_right_pressed():
            dx = 1

        if self.is_up_pressed():
            dy = -1

        if self.is_down_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        return raylibpy.window_should_close()

# Reference
# Input-related functions: mouse
#     bool IsMouseButtonPressed(int button);                                  // Check if a mouse button has been pressed once
#     bool IsMouseButtonDown(int button);                                     // Check if a mouse button is being pressed
#     bool IsMouseButtonReleased(int button);                                 // Check if a mouse button has been released once
#     bool IsMouseButtonUp(int button);                                       // Check if a mouse button is NOT being pressed
#     int GetMouseX(void);                                                    // Get mouse position X
#     int GetMouseY(void);                                                    // Get mouse position Y
#     Vector2 GetMousePosition(void);                                         // Get mouse position XY
#     Vector2 GetMouseDelta(void);                                            // Get mouse delta between frames
#     void SetMousePosition(int x, int y);                                    // Set mouse position XY
#     void SetMouseOffset(int offsetX, int offsetY);                          // Set mouse offset
#     void SetMouseScale(float scaleX, float scaleY);                         // Set mouse scaling
#     float GetMouseWheelMove(void);                                          // Get mouse wheel movement Y
#     void SetMouseCursor(int cursor);                                        // Set mouse cursor
