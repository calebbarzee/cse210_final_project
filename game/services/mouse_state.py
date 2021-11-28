from game.point import Point
from game.input_service import InputService


class Mouse_State():

    def __init__(self):
        self._previous_mouse_location = Point(0, 0)
        self._current_mouse_location = Point(0, 0)
        self._state = "waiting"
        self._drag_cycle = 0

    def drag_state(self, recyclable):
        # SET previous mouse location
        # SET current mouse location
        # IF mouse button is pressed and within object space
        #   SET state = dragging state
        # ELSE
        #   SET state = waiting
        # IF state == dragging state & drag_cycle == 1
        # 		SET velocity = (difference between previous mouse location current location)
        # ELSE IF state == dragging state & drag_cycle == 0
        # 		SET velocity = (0, 0)
        # 		SET drag_cycle = 1
        #
        # ELSE IF state == waiting & drag_cycle == 1
        # 	SET velocity = (0, 1)
        #   SET drag_cycle = 0
        #
        self._previous_mouse_location = self._current_mouse_location
        self._current_mouse_location = InputService.mouse_location
        is_within = recyclable.is_within_bounding_box(
            self._current_mouse_location)
        if InputService.mouse_button_pressed and is_within:
            self._state = "dragging"
        else:
            self._state = "waiting"
        if self._state == "dragging" and self._drag_cycle == 1:
            x_difference = self._current_mouse_location.get_x - \
                self._previous_mouse_location.get_x
            y_difference = self._current_mouse_location.get_y - \
                self._previous_mouse_location.get_y
            recyclable.set_velocity(Point(x_difference, y_difference))
        elif self._state == "dragging" and self._drag_cycle == 0:
            recyclable.set_velocity(Point(0, 0))
            self._drag_cycle = 1
        elif self._state == "waiting" and self._drag_cycle == 1:
            recyclable.set_velocity(Point(0, 1))
            self._drag_cycle = 0