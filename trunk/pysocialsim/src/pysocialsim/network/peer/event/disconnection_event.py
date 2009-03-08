from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent

class DisconnectionEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("DISCONNECT_PEER", peer, priority)
        