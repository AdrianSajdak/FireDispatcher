from state.free_state import FreeState
from state.busy_state import BusyState
from state.returning_state import ReturningState

class CarStateContext:
    def __init__(self):
        self._current_state = FreeState()

    def set_busy(self):
        self._current_state = BusyState()

    def set_free(self):
        self._current_state = FreeState()

    def set_returning(self):
        self._current_state = ReturningState()

    def is_free(self) -> bool:
        return self._current_state.is_free()

    def is_busy(self) -> bool:
        return self._current_state.is_busy()

    def is_returning(self) -> bool:
        return self._current_state.is_returning()

    def get_current_state_name(self) -> str:
        return self._current_state.get_state_name()
