"""
Defines the module with the implementation of AbstractPeerToPeerMessage class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 07/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from pysocialsim.common.base.decorators import public
from copy import copy
from pysocialsim.common.util.rotines import returns

class AbstractPeertoPeerMessage(Object, IPeerToPeerMessage):
    """
    Defines the default implementation of IPeerToPeerMessage interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 07/10/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, handle):
        """
        Initializes peer-to-peer messages.
        @param handle: the handle of peer-to-peer message
        @type handle: str
        """
        self.__handle = handle
        

    @public
    def getHandle(self):
        return self.__handle

    @public
    def getId(self):
        return self.__id

    @public
    def getSourceId(self):
        return self.__sourceId

    @public
    def getTargetId(self):
        return self.__targetId

    @public
    def getTTL(self):
        return self.__ttl

    @public
    def getPriority(self):
        return self.__priority

    @public
    def getHop(self):
        return self.__hop

    @public
    def setHop(self, value):
        self.__hop = value
    
    @public    
    def init(self, id, sourceId, targetId, ttl, priority):
        self.__id = id
        self.__sourceId = sourceId
        self.__targetId = targetId
        self.__ttl = ttl
        self.__priority = priority
        self.__hop = 0
    
    @public
    def clone(self):
        return returns(copy(self), IPeerToPeerMessage)

    handle = property(getHandle, None, None, None)

    id = property(getId, None, None, None)

    sourceId = property(getSourceId, None, None, None)

    targetId = property(getTargetId, None, None, None)

    ttl = property(getTTL, None, None, None)

    priority = property(getPriority, None, None, None)

    hop = property(getHop, setHop, None, None)
    