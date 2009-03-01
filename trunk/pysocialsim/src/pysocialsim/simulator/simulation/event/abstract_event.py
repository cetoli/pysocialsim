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
    def initialize(self, handle, peer):
        self.__handle = handle
        self.__peer = peer
        
    @public
    @return_type(str)
    def getHandle(self):
        return self.__handle
    
    @public
    @return_type(Peer)
    def getPeer(self):
        return self.__peer