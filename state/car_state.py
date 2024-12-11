from abc import ABC, abstractmethod

class CarState(ABC):

    @abstractmethod
    def set_busy(self):
        pass

    @abstractmethod
    def set_free(self):
        pass

    @abstractmethod
    def set_returning(self):
        pass

    @abstractmethod
    def is_free(self) -> bool:
        pass

    @abstractmethod
    def is_busy(self) -> bool:
        pass

    @abstractmethod
    def is_returning(self) -> bool:
        pass

    @abstractmethod
    def get_state_name(self) -> str:
        pass
