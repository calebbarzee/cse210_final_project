def evaluate_recyclables_state(self):
    for actor in self._cast:
        if actor._type == "recyclable":
            self._object_state.drag_state(actor)
            self._object_state.clear_recyclable(
                actor, self._cast, self._health, self._score)


class ClearRecyclablesAction(Action):

    def __init__(self, cast, health, score):
        super().__init__()
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
            i = cast.index(recyclable)
            cast.pop(i)
