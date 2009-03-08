from pysocialsim.simulator.simulation.event.default_event import DefaultEvent

class ConnectionEvent(DefaultEvent):
    
    def __init__(self, peer, priority):
        self.initialize("CONNECT_PEER", peer, priority)