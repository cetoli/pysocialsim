from pysocialsim.simulator.event.abstract_event import AbstractEvent
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
from pysocialsim.base.decorator.public import public

class AbstractPeerEvent(AbstractEvent):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, handle, peer, priority, message):
        AbstractEvent.initialize(self, handle, peer, priority)
        self.__message = message
        
    @public
    def getP2PMessage(self):
        return self.__message