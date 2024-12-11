# FIREDEP/observer/skkm.py

from observer.observed_subject import ObservedSubject
from model.event_type import EventType

class SKKM(ObservedSubject):
    def __init__(self):
        self._observers = []

    def add_observer(self, o):
        self._observers.append(o)

    def remove_observer(self, o):
        self._observers.remove(o)

    def notify_all(self, event):
        # Ta metoda nie będzie już używana do bezpośredniego powiadamiania wszystkich.
        # Zostawiamy jako pustą lub informacyjną.
        pass

    def handle_event(self, event):
        # Wybór liczby potrzebnych pojazdów na podstawie typu zdarzenia
        if event.type == EventType.PZ:
            needed_cars = 3
        elif event.type == EventType.MZ:
            needed_cars = 2
        else:
            # Dla AF nie dysponujemy od razu pojazdów - ale AF wychodzi dopiero po dojeździe.
            # Jeśli jednak pojawiłby się AF, to potrzebne_cars = 0
            needed_cars = 0

        if needed_cars == 0:
            print(f"[SKKM] Zdarzenie {event} nie wymaga dysponowania pojazdów.")
            return

        # Sortowanie jednostek po odległości do zdarzenia
        stations_sorted = sorted(self._observers, key=lambda s: s.distance_to(event.location))

        dispatched_cars_total = []
        stations_used = []

        # Próbujemy pobrać potrzebną liczbę pojazdów z najbliższych jednostek
        for station in stations_sorted:
            dispatched = station.try_dispatch_cars(needed_cars - len(dispatched_cars_total))
            if dispatched is not None:
                dispatched_cars_total.extend(dispatched)
                stations_used.append((station, dispatched))
            if len(dispatched_cars_total) == needed_cars:
                break

        if len(dispatched_cars_total) < needed_cars:
            print(f"[SKKM] Nie udało się uzyskać wymaganych {needed_cars} pojazdów dla {event}. Brak dysponowania.")
            # Przywracamy pojazdy do wolnych, jeśli jakieś częściowo pobraliśmy (rzadki przypadek)
            for st, cars in stations_used:
                st.return_vehicles(cars, instant=True)
            return

        # Mamy wystarczającą liczbę pojazdów rozlokowaną w stations_used.
        print(f"[SKKM] Do zdarzenia {event} zadysponowano łącznie {len(dispatched_cars_total)} pojazdy.")
        for st, cars in stations_used:
            st.handle_dispatched_event(event, cars)
