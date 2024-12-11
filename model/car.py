from state.car_state_context import CarStateContext

class Car:
    def __init__(self, car_id: str):
        self._id = car_id
        self._state_context = CarStateContext()

    def set_busy(self):
        self._state_context.set_busy()

    def set_free(self):
        self._state_context.set_free()

    def set_returning(self):
        self._state_context.set_returning()

    def is_free(self) -> bool:
        return self._state_context.is_free()

    def is_busy(self) -> bool:
        return self._state_context.is_busy()

    def is_returning(self) -> bool:
        return self._state_context.is_returning()

    def __str__(self):
        return f"({self._id})"
