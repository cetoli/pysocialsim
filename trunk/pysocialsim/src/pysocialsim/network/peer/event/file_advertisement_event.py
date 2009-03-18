from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent

class FileAdvertisementEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("FILE_ADVERTISEMENT", peer, priority)