"""
Defines the module with the specification of IPeer interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""

class IPeer(object):
    """
    Defines the interface of peer objects.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self):
        """
        @raise NotImplementedError: Interfaces can't be instantiated.
        """
        raise NotImplementedError()
    
    def getId(self):
        """
        Gets the peer identifier.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getType(self):
        """
        Gets the type of peer.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
    
    def isJoined(self):
        raise NotImplementedError()
    
    def isLeaved(self):
        raise NotImplementedError()
    
    def setNode(self, node):
        raise NotImplementedError()
    
    def getNode(self):
        raise NotImplementedError()
    
    def joined(self):
        raise NotImplementedError()
    
    def leaved(self):
        raise NotImplementedError()
    
    def join(self):
        raise NotImplementedError()
    
    def receive(self, peerToPeerMessage):
        raise NotImplementedError()
    
    def send(self, peerToPeerMessage):
        raise NotImplementedError()
    
    def getPeerToPeerNetwork(self):
        raise NotImplementedError()
    
    def addNeighbor(self, neighbor):
        raise NotImplementedError()
    
    def removeNeighbor(self, peerId):
        raise NotImplementedError()
    
    def countNeighbors(self):
        raise NotImplementedError()
    
    def hasNeighbor(self, peerId):
        raise NotImplementedError()
    
    def getNeighbor(self, peerId):
        raise NotImplementedError()
    
    def getPeerToPeerProtocol(self):
        raise NotImplementedError()
    
    def configure(self, peerToPeerMessageHandlers):
        raise NotImplementedError()
    
    def getNeighbors(self):
        raise NotImplementedError()
    
    def getPeerToPeerMessageDispatcher(self):
        raise NotImplementedError()
    
    def route(self, peerToPeerMessage):
        raise NotImplementedError()
    
    def leave(self):
        raise NotImplementedError()