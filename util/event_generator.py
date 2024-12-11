from model.event import Event
from model.event_type import EventType
from model.location import Location
from util.probability_utils import random_boolean, random_double

class EventGenerator:
    LAT_MIN = 49.95855025648944
    LAT_MAX = 50.154564013341734
    LON_MIN = 19.688292482742394
    LON_MAX = 20.02470275868903

    def generate_event(self):
        lat = random_double(self.LAT_MIN, self.LAT_MAX)
        lon = random_double(self.LON_MIN, self.LON_MAX)
        location = Location(lat, lon)

        is_mz = random_boolean(0.7)
        event_type = EventType.MZ if is_mz else EventType.PZ
        return Event(event_type, location)
