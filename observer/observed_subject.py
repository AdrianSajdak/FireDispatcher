from abc import ABC, abstractmethod

class ObservedSubject(ABC):
    @abstractmethod
    def add_observer(self, o):
        pass

    @abstractmethod
    def remove_observer(self, o):
        pass

    @abstractmethod
    def notify_all(self, event):
        pass
