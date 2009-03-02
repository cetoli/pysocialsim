from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.peer.peer import Peer
from pysocialsim.base.decorator.require import require

class AbstractEvent(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("handle", str)
    @require("peer", Peer)
    @require("priority", int)
    def initialize(self, handle, peer, priority):
        self.__handle = handle
        self.__peer = peer
        self.__priority = priority
        
    @public
    @return_type(str)
    def getHandle(self):
        return self.__handle
    
    @public
    @return_type(Peer)
    def getPeer(self):
        return self.__peer
    
    @public
    @return_type(int)
    def getPriority(self):
        return self.__priority