from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.message.message import Message
from types import NoneType
from pysocialsim.base.decorator.require import require
from pysocialsim.network.peer.peer import Peer

class AbstractPeerEvent(AbstractEvent):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(NoneType)
    @require("handle", str)
    @require("peer", Peer)
    @require("priority", int)
    @require("message", Message)
    def initialize(self, handle, peer, priority, message):
        AbstractEvent.initialize(self, handle, peer, priority)
        self.__message = message
        
    @public
    @return_type(Message)
    def getMessage(self):
        return self.__message