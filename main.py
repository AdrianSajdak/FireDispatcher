# FIREDEP/main/main.py

import threading
import time
from observer.skkm import SKKM
from model.fire_station import FireStation
from util.event_generator import EventGenerator

def main():
    skkm = SKKM()

    stations = [
        FireStation("JRG-1", 50.05996349986543, 19.94312747506376),
        FireStation("JRG-2", 50.03340338319642, 19.935842217105698),
        FireStation("JRG-3", 50.07572790077249, 19.887342293797523),
        FireStation("JRG-4", 50.03771138716599, 20.005759039439887),
        FireStation("JRG-5", 50.09182826406526, 19.919937532126315),
        FireStation("JRG-6", 50.01614511919627, 20.015608186637632),
        FireStation("JRG-7", 50.09410608938052, 19.97742159248123),
        FireStation("JRG-SA-PSP", 50.07716027811056, 20.032791523895515),
        FireStation("JRG-Skawina", 49.96840295351511, 19.799435392275186),
        FireStation("LSP-Balice", 50.07872791095225, 19.788759688574586)
    ]

    for s in stations:
        skkm.add_observer(s)

    generator = EventGenerator()

    event_thread = threading.Thread(target=generator.event_generation_loop, args=(skkm,), daemon=True)
    event_thread.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
