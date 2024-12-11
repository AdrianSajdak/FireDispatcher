from strategy.i_event_dispatch_strategy import IEventDispatchStrategy

class LocalHazardDispatchStrategy(IEventDispatchStrategy):
    def dispatch_units(self, event, stations):
        for st in stations:
            if st.dispatch_cars(2):
                return True
        return False
