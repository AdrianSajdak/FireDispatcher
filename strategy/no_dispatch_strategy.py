from strategy.i_event_dispatch_strategy import IEventDispatchStrategy

class NoDispatchStrategy(IEventDispatchStrategy):
    def dispatch_units(self, event, stations):
        return False
