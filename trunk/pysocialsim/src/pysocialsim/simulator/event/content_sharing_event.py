from pysocialsim.simulator.event.abstract_event import AbstractEvent

class ContentSharingEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("SHARE_CONTENT", peer, priority)
        
    