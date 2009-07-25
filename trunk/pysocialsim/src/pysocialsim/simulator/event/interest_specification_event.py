from pysocialsim.simulator.event.abstract_event import AbstractEvent

class InterestSpecificationEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("INTEREST_SPECIFICATION", peer, priority)
