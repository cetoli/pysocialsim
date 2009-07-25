from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.base.interface import Interface

class IPeerEvent(IEvent):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getP2PMessage(self):
        raise NotImplementedError()