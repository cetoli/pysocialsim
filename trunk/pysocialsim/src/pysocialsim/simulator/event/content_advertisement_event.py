from pysocialsim.simulator.event.abstract_event import AbstractEvent

class ContentAdvertisementEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("ADVERTISE_CONTENT", peer, priority)