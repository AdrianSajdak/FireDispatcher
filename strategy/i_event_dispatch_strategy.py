from abc import ABC, abstractmethod

class IEventDispatchStrategy(ABC):

    @abstractmethod
    def dispatch_units(self, event, stations):
        pass
