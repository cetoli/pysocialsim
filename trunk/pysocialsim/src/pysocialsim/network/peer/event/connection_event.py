from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent

class ConnectionEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("CONNECT_PEER", peer, priority)