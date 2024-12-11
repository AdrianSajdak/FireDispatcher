from abc import ABC, abstractmethod

class VehicleAggregate(ABC):

    @abstractmethod
    def create_iterator(self):
        pass
