from game.point import Point
from game import constants
from game.services.input_service import InputService


class Object_State():

    def __init__(self):
        self._input_service = InputService()
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
        self._current_mouse_location = self._input_service.mouse_location()
        is_within = recyclable.is_within_bounding_box(
            self._current_mouse_location)
        if InputService.mouse_button_pressed and is_within:
            self._state = "dragging"
        else:
            self._state = "falling"
        if self._state == "dragging" and self._drag_cycle == 1:
            x_difference = self._current_mouse_location.get_x - \
                self._previous_mouse_location.get_x
            y_difference = self._current_mouse_location.get_y - \
                self._previous_mouse_location.get_y
            recyclable.set_velocity(Point(x_difference, y_difference))
        elif self._state == "dragging" and self._drag_cycle == 0:
            recyclable.set_velocity(Point(0, 0))
            self._drag_cycle = 1
        elif self._state == "falling" and self._drag_cycle == 1:
            recyclable.set_velocity(Point(0, 1))
            self._drag_cycle = 0
        if recyclable._position.get_y() > 1100:
            self._state = "waiting"
            recyclable.set_velocity(Point(0, 0))

    def clear_recyclable(self, recyclable, cast, health, score):
        if self._state == "waiting":
            x = recyclable.position.get_x
            if x in range(0, 300):
                # ^^^ paper bin range
                if recyclable._recyclable_type == "paper":
                    points = 10
                    value = 0
                else:
                    points = 0
                    value = -5
            elif x in range(300, 600):
                # ^^^ glass bin range
                if recyclable._recyclable_type == "glass":
                    points = 10
                    value = 0
                else:
                    points = 0
                    value = -5

            elif x in range(600, 900):
                # ^^^ metal bin range
                if recyclable._recyclable_type == "metal":
                    points = 10
                    value = 0
                else:
                    points = 0
                    value = -5
            health.update_health(value)
            score.update_score(points)
            cast.pop(recyclable)
