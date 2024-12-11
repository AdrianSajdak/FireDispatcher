class VehicleIterator:
    def __init__(self, cars):
        self._cars = cars
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position < len(self._cars):
            car = self._cars[self._position]
            self._position += 1
            return car
        else:
            raise StopIteration
