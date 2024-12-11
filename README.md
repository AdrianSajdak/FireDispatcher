# Fire Department Dispatcher Simulation

## Opis
Projekt symuluje dysponowanie sił i środków Państwowej Straży Pożarnej na obszarze miasta Krakowa.  
Wykorzystane zostały wzorce projektowe:
- **Strategia** (wybór sposobu dysponowania pojazdów w zależności od typu zdarzenia),
- **Obserwator** (SKKM jako podmiot obserwowany, jednostki straży jako obserwatorzy),
- **Stan** (stan pojazdu: wolny, zajęty, powracający),
- **Iterator** (iteracja po kolekcji pojazdów w jednostce).

Zdarzenia generowane są co 15-35 sekund. Po każdym wygenerowaniu zdarzenia SKKM decyduje, które i ile pojazdów z najbliżej położonych jednostek zadysponować. Pojazdy dojeżdżają na miejsce zdarzenia (czas 0-3s), sprawdzane jest, czy jest to alarm fałszywy (5% szans):
- Jeśli alarm jest fałszywy, pojazdy wracają natychmiast.
- Jeśli nie, podejmowane są działania (5-25s), po których pojazdy wracają do jednostek (0-3s).

Wszystkie istotne informacje (dysponowanie pojazdów, dojazd, podjęcie działań, powrót) są logowane w konsoli.

## Wymagania
- Python 3.8+ (rekomendowany)
- Biblioteki standardowe (brak dodatkowych zewnętrznych zależności)

## Struktura katalogów

    FIREDEPARTMENTDISPATCHER/
    ├─ main.py
    │ ├─ model/ 
    │   ├─ car.py 
    │   ├─ event.py 
    │   ├─ event_type.py 
    │   ├─ fire_station.py 
    │   ├─ location.py 
    │   ├─ vehicle_aggregate.py 
    │   └─ vehicle_iterator.py 
    │ ├─ observer/ 
    │   ├─ observed_subject.py 
    │   ├─ observer.py 
    │   └─ skkm.py 
    │ ├─ state/ 
    │   ├─ busy_state.py 
    │   ├─ car_state.py 
    │   ├─ car_state_context.py 
    │   ├─ free_state.py 
    │   └─ returning_state.py 
    │ ├─ strategy/ 
    │   ├─ fire_dispatch_strategy.py 
    │   ├─ i_event_dispatch_strategy.py 
    │   ├─ local_hazard_dispatch_strategy.py 
    │   └─ no_dispatch_strategy.py 
    │ ├─ util/ 
    │   ├─ event_generator.py 
    │   ├─ probability_utils.py 
    │   └─ time_utils.py 
    │ ├─ README.md



## Uruchomienie
1. Przejdź do głównego katalogu `FIREDEP`.
2. Upewnij się, że masz zainstalowaną wymaganą wersję Pythona.
3. Uruchom symulację poleceniem:
   ```bash
   python main.py
