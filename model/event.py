class Event:
    def __init__(self, event_type, location):
        self._type = event_type
        self._location = location

    @property
    def type(self):
        return self._type

    @property
    def location(self):
        return self._location

    def __str__(self):
        return f"({self._type.value}, {self._location})"