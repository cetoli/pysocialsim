from pysocialsim.simulator.event.abstract_event import AbstractEvent

class RelationshipCreationEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("RELATIONSHIP_CREATION", peer, priority)