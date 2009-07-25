from pysocialsim.simulator.event.abstract_event import AbstractEvent

class PeerDisconnectionEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("DISCONNECT_PEER", peer, priority)