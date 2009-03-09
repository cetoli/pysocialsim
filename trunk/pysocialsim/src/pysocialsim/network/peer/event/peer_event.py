from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.interface import Interface

class PeerEvent(Event):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getMessage(self):
        raise NotImplementedError()