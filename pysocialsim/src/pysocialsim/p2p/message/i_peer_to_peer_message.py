"""
Defines the module with the specification of IPeerToPeerMessage.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 07/10/2009
"""

class IPeerToPeerMessage(object):
    
    ADVERTISEMENT = 0
    QUERY = 1
    SERVICE = 2
    SYSTEM = 3
    
    def __init__(self):
        raise NotImplementedError()
    
    def getSourceId(self):
        """
        Gets the identifier of source peer.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getTargetId(self):
        """
        Gets the identifier of target peer.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getTTL(self):
        """
        Gets the time to live of message.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getHop(self):
        """
        Gets the number of hops.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def setHop(self, hop):
        """
        Gets the number of hops.
        @param hop: number of hops
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def clone(self):
        """
        Create a copy of peer-to-peer message.
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def getHandle(self):
        """
        Gets the handle of peer-to-peer message.
        @return: a str
        @rtype: str
        """
        raise NotImplementedError()
    
    def getId(self):
        """
        Gets the identifier of peer-to-peer message.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getPriority(self):
        """
        Gets the priority of peer-to-peer message.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def init(self, id, sourceId, targetId, ttl, priority):
        """
        Initializes peer-to-peer messages.
        @param id: the identifier of peer-to-peer message
        @type id: int
        @param sourceId: source identifier of peer-to-peer message
        @type sourceId: int
        @param targetId: target identifier of peer-to-peer message
        @type targetId: int
        @param ttl: time-to-live of peer-to-peer message
        @type ttl: int
        @param priority: priority of peer-to-peer message
        @type priority: int
        """
        raise NotImplementedError()
    
    def getType(self):
        """
        Gets the type of message.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def registerPeerId(self, peerId):
        raise NotImplementedError()
    
    def unregisterPeerId(self, peerId):
        raise NotImplementedError()
    
    def countPeerIds(self):
        raise NotImplementedError()
    
    def hasPeerId(self, peerId):
        raise NotImplementedError()
    
    def getPeerIds(self):
        raise NotImplementedError()
    
    def getFirst(self):
        raise NotImplementedError()
    
    def getLast(self):
        raise NotImplemented()
    
    def registerParameter(self, name, value):
        raise NotImplementedError()
    
    def getParameter(self, name):
        raise NotImplementedError()
    
    def unregisterParameter(self, name):
        raise NotImplementedError()
    
    def countParameters(self):
        raise NotImplementedError()
    
    def getParameterNames(self):
        raise NotImplementedError()
    
    def getParameterValues(self):
        raise NotImplementedError()
    
    def hasParameter(self, name):
        raise NotImplementedError()
    
    def getSize(self):
        raise NotImplementedError()
    
    def setTime(self, time):
        raise NotImplementedError()
    
    def getTime(self):
        raise NotImplementedError()