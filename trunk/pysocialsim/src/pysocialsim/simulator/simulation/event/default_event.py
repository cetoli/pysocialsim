from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent

class DefaultEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("DEFAULT", peer, priority)