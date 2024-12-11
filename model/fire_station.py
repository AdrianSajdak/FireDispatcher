# FIREDEP/model/fire_station.py

import threading
import time
from model.vehicle_aggregate import VehicleAggregate
from model.vehicle_iterator import VehicleIterator
from model.car import Car
from util.time_utils import sleep
from util.probability_utils import random_int, random_boolean

class FireStation(VehicleAggregate):
    def __init__(self, name: str, lat: float, lon: float):
        from model.location import Location
        self._name = name
        self._location = Location(lat, lon)
        self._cars = [Car(f"{self._name}-Car{i}") for i in range(1,6)]
        self._lock = threading.Lock()

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def distance_to(self, other):
        return self._location.distance_to(other)

    def try_dispatch_cars(self, count: int):
        """Próbuje pobrać 'count' wolnych pojazdów. Zwraca listę pojazdów lub None jeśli się nie uda."""
        with self._lock:
            free_cars = [c for c in self._cars if c.is_free()]
            if len(free_cars) < count:
                return None
            # Pobieramy 'count' pojazdów i ustawiamy je jako Busy
            selected = free_cars[:count]
            for c in selected:
                c.set_busy()
            print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Zadysponowano {count} pojazdy: {', '.join(str(c) for c in selected)}")
            return selected

    def handle_dispatched_event(self, event, dispatched_cars):
        # Uruchamiamy wątek symulujący przebieg akcji
        t = threading.Thread(target=self._event_action_thread, args=(event, dispatched_cars,))
        t.start()

    def _event_action_thread(self, event, dispatched_cars):
        # Symulujemy dojazd
        travel_time = random_int(0,3)
        print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Pojazdy {', '.join(str(c) for c in dispatched_cars)} "
              f"wyruszyły do zdarzenia {event}. Czas dojazdu: ~{travel_time}s")
        sleep(travel_time)

        # Sprawdzamy alarm fałszywy 5%
        if random_boolean(0.05):
            print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Alarm fałszywy dla: {event}, pojazdy wracają")
            self.return_vehicles(dispatched_cars)
            return

        # Działania (5-25s)
        action_time = random_int(5,25)
        print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Rozpoczęto działania: {event} (ok. {action_time}s)")
        sleep(action_time)
        print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Zakończono działania: {event}")

        self.return_vehicles(dispatched_cars)

    def return_vehicles(self, cars_list, instant=False):
        return_time = 0 if instant else random_int(0,3)
        if return_time > 0:
            print(f"[{time.strftime('%H:%M:%S')}] {self._name}: Pojazdy wracają, dojazd do jednostki ~{return_time}s")
        sleep(return_time)
        with self._lock:
            for c in cars_list:
                c.set_free()
            print(f"[{time.strftime('%H:%M:%S')}] {self._name}: {', '.join(str(c) for c in cars_list)} powróciły do jednostki i są teraz dostępne.")

    def create_iterator(self):
        return VehicleIterator(self._cars)
