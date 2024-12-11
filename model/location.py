import math

class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other) -> float:
        dx = other.longitude - self.longitude
        dy = other.latitude - self.latitude
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f"({self.latitude:.4f}, {self.longitude:.4f})"
