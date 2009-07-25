from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.peer.i_peer import IPeer
from types import NoneType

class AbstractEvent(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, handle, peer, priority):
        self.__handle = handle
        self.__peer = peer
        self.__priority = priority
        self.__isHandled = False
    
    @public
    def getHandle(self):
        return self.__handle
    
    @public
    def getPeer(self):
        return self.__peer
    
    @public
    def getPriority(self):
        return self.__priority
    
    @public
    def handled(self):
        self.__isHandled = True
    
    @public
    def unhandled(self):
        self.__isHandled = False
    
    @public
    def isHandled(self):
        return self.__isHandled
    
    def __eq__(self, other):
        return (self.__handle and other.getHandle()) and (self.__peer == other.getPeer()) and (self.__priority == other.getPriority()) and (self.__isHandled == other.isHandled()) 