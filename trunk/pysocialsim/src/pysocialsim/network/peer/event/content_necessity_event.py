from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent

class ContentNecessityEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("CONTENT_NECESSITY", peer, priority)