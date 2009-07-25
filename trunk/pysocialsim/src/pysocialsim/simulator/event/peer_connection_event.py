from pysocialsim.simulator.event.abstract_event import AbstractEvent

class PeerConnectionEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("CONNECT_PEER", peer, priority)