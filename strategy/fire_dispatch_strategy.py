from strategy.i_event_dispatch_strategy import IEventDispatchStrategy

class FireDispatchStrategy(IEventDispatchStrategy):
    def dispatch_units(self, event, stations):
        for st in stations:
            if st.dispatch_cars(3):
                return True
        return False
