"""
Defines the module with the implementation of AbstractPeerToPeerMessage class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 07/10/2009
"""
from pysocialsim.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
import zlib
import pickle

class AbstractPeertoPeerMessage(IPeerToPeerMessage):
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
        

    
    def getHandle(self):
        return self.__handle

    
    def getId(self):
        return self.__id

    
    def getSourceId(self):
        return self.__sourceId

    
    def getTargetId(self):
        return self.__targetId

    
    def getTTL(self):
        return self.__ttl

    
    def getPriority(self):
        return self.__priority

    
    def getHop(self):
        return self.__hop

    
    def setHop(self, value):
        self.__hop = value
    
        
    def init(self, id, sourceId, targetId, ttl, priority, size, time):
        self.__id = id
        self.__sourceId = sourceId
        self.__targetId = targetId
        self.__ttl = ttl
        self.__priority = priority
        self.__hop = 0
        self.__size = size
        self.__time = time
        
    
    
    def clone(self):
        msgClone = self.__class__()
        msgClone.init(self.__id, self.__sourceId, self.__targetId, self.__ttl, self.__priority, self.__size, self.__time)
        msgClone.setHop(self.__hop)
        for peerId in self.__peerIds:
            msgClone.registerPeerId(peerId)
        for name in self.__parameters.keys():
            msgClone.registerParameter(name, self.__parameters[name])
        return msgClone
    
    
    def getType(self):
        return self.__type
    
    
    def registerPeerId(self, peerId):
        if peerId in self.__peerIds:
            return False
        
        self.__peerIds.append(peerId)
        return peerId in self.__peerIds

    
    def unregisterPeerId(self, peerId):
        if not peerId in self.__peerIds:
            return False
        self.__peerIds.remove(peerId)
        return not peerId in self.__peerIds

    
    def countPeerIds(self):
        return len(self.__peerIds)

    
    def hasPeerId(self, peerId):
        return peerId in self.__peerIds

    
    def getPeerIds(self):
        peerIds = []
        peerIds += self.__peerIds
        return peerIds
    
    
    def getFirst(self):
        if len(self.__peerIds) == 0:
            return None
        return self.__peerIds[0]
    
    
    def getLast(self):
        if len(self.__peerIds) == 0:
            return None
        return self.__peerIds[len(self.__peerIds) - 1]
    
    
    def registerParameter(self, name, value):
        self.__parameters[name] = value
    
    
    def getParameter(self, name):
        return self.__parameters[name]
    
    
    def unregisterParameter(self, name):
        del self.__parameters[name]
    
    
    def countParameters(self):
        return len(self.__parameters)
    
    
    def getParameterNames(self):
        return self.__parameters.keys()
    
    
    def getParameterValues(self):
        return self.__parameters.values()
    
    
    def getSize(self):
        return self.__size
    
    
    def hasParameter(self, name):
        return self.__parameters.has_key(name)
    
    
    def getTime(self):
        return self.__time

    
    def setTime(self, time):
        self.__time = time
        return self.__time
    
    def __eq__(self, other):
        return self.__id == other.getId()