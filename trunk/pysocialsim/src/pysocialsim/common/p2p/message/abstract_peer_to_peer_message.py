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
from pysocialsim.common.util.rotines import returns, requires, pre_condition
import zlib
import pickle

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

    def initialize(self, type, handle, size):
        """
        Initializes peer-to-peer messages.
        @param type: the type of message
        @type type: int
        @param handle: the handle of peer-to-peer message
        @type handle: str
        """
        self.__type = type
        self.__handle = handle
        self.__sourceId = ""
        self.__targetId = ""
        self.__ttl = 0
        self.__priority = 0
        self.__hop = 0
        self.__id = ""
        self.__peerIds = []
        self.__parameters = {}
        self.__size = size
        self.__time = 0.0
        

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
    def init(self, id, sourceId, targetId, ttl, priority, size, time):
        self.__id = id
        self.__sourceId = sourceId
        self.__targetId = targetId
        self.__ttl = ttl
        self.__priority = priority
        self.__hop = 0
        self.__size = size
        self.__time = time
        
    
    @public
    def clone(self):
        msgClone = self.__class__()
        msgClone.init(self.__id, self.__sourceId, self.__targetId, self.__ttl, self.__priority, self.__size, self.__time)
        msgClone.setHop(self.__hop)
        for peerId in self.__peerIds:
            msgClone.registerPeerId(peerId)
        for name in self.__parameters.keys():
            msgClone.registerParameter(name, self.__parameters[name])
        return returns(msgClone, IPeerToPeerMessage)
    
    @public
    def getType(self):
        return self.__type
    
    @public
    def registerPeerId(self, peerId):
        requires(peerId, str)
        
        if peerId in self.__peerIds:
            return False
        
        self.__peerIds.append(peerId)
        return peerId in self.__peerIds

    @public
    def unregisterPeerId(self, peerId):
        requires(peerId, str)
        if not peerId in self.__peerIds:
            return False
        self.__peerIds.remove(peerId)
        return not peerId in self.__peerIds

    @public
    def countPeerIds(self):
        return returns(len(self.__peerIds), int)

    @public
    def hasPeerId(self, peerId):
        requires(peerId, str)
        return peerId in self.__peerIds

    @public
    def getPeerIds(self):
        peerIds = []
        peerIds += self.__peerIds
        return peerIds
    
    @public
    def getFirst(self):
        if len(self.__peerIds) == 0:
            return None
        return self.__peerIds[0]
    
    @public
    def getLast(self):
        if len(self.__peerIds) == 0:
            return None
        return self.__peerIds[len(self.__peerIds) - 1]
    
    @public
    def registerParameter(self, name, value):
        self.__parameters[name] = value
    
    @public
    def getParameter(self, name):
        return self.__parameters[name]
    
    @public
    def unregisterParameter(self, name):
        del self.__parameters[name]
    
    @public
    def countParameters(self):
        return len(self.__parameters)
    
    @public
    def getParameterNames(self):
        return self.__parameters.keys()
    
    @public
    def getParameterValues(self):
        return self.__parameters.values()
    
    @public
    def getSize(self):
        return self.__size
    
    @public
    def hasParameter(self, name):
        return self.__parameters.has_key(name)
    
    @public
    def getTime(self):
        return self.__time

    @public
    def setTime(self, time):
        self.__time = time
        return self.__time
    
    def __eq__(self, other):
        return self.__id == other.getId()


    handle = property(getHandle, None, None, None)

    id = property(getId, None, None, None)

    sourceId = property(getSourceId, None, None, None)

    targetId = property(getTargetId, None, None, None)

    ttl = property(getTTL, None, None, None)

    priority = property(getPriority, None, None, None)

    hop = property(getHop, setHop, None, None)

    type = property(getType, None, None, None)    
    size = property(getSize, None, None, None)

    time = property(getTime, setTime, None, None)
