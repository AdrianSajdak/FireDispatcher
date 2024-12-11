from state.car_state import CarState

class BusyState(CarState):
    def set_busy(self):
        pass

    def set_free(self):
        pass

    def set_returning(self):
        pass

    def is_free(self) -> bool:
        return False

    def is_busy(self) -> bool:
        return True

    def is_returning(self) -> bool:
        return False

    def get_state_name(self) -> str:
        return "Busy"
