"""
Defines the module with the specification IPeerToPeerNetwork interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""

class IPeerToPeerNetwork(object):
    """
    Defines the interface of peer-to-peer network.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 29/08/2009
    """
    SUPER_PEER = 0
    """
    @cvar: Identifies the super peer type.
    @type: int 
    """
    SIMPLE_PEER = 1
    """
    @cvar: Identifies the simple peer type.
    @type: int 
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    
    
    def getSimulation(self):
        """
        Gets a simulation object.
        @return: an ISimulation
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def setSimulation(self, simulation):
        """
        Sets a simulation object.
        @param simulation: an ISimulation
        @type simulation: ISimulation
        @return: an ISimulation
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def addPeer(self, peerType, peer):
        """
        Adds a peer in peer-to-peer network.
        @param peerType: type of peer
        @type peerType: int
        @param peer: a IPeer
        @type peer: IPeer
        @return: Returs True, if peer was added in peer-to-peer network. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def removePeer(self, peerType, peerId):
        """
        Gets a peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer identifier
        @type peerId: str
        @return: Returs True, if peer was removed in peer-to-peer network. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def getPeer(self, peerType, peerId):
        """
        Gets a peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer identifier
        @type peerId: int
        @return: a IPeer
        @rtype: IPeer
        """
        raise NotImplementedError()
    
    def getPeers(self, peerType):
        """
        Gets the list of peers, according to type of peer
        @param peerType: the type of peer
        @type peerType: int
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def countPeers(self, peerType):
        """
        Gets the number of peers, according to type of peer
        @param peerType: the type of peer
        @type peerType: int
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getConnectedPeers(self, peerType):
        """
        Gets the list of connected peers in network.
        @param peerType: the type of peer
        @type peerType: int
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def getDisconnectedPeers(self, peerType):
        """
        Gets the list of disconnected peers in network.
        @param peerType: the type of peer
        @type peerType: int
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def setConnectionsBetweenSuperPeers(self, numberOfConnections):
        """
        Sets the number of connections between super peers.
        @param numberOfConnections: the number of connections
        @type numberOfConnections: int
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getConnectionsBetweenSuperPeers(self):
        """
        Gets the number of connections between super peers.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def registerPeerToPeerProtocol(self, peerType, peerToPeerProtocol):
        """
        Registers the peer-to-peer protocol by type of peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerToPeerProtocol: an IPeerToPeerProtocol
        @type peerToPeerProtocol: IPeerToPeerProtocol
        @return: Returns True, if peer-to-peer protocol was registered. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def unregisterPeerToPeerProtocol(self, peerType):
        """
        Unregisters the peer-to-peer protocol by type of peer.
        @param peerType: the type of peer
        @type peerType: int
        @return: Returns True, if peer-to-peer protocol was unregistered. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def getPeerToPeerProtocol(self, peerType):
        """
        Gets the peer-to-peer protocol by type of peer.
        @param peerType: the type of peer
        @type peerType: int
        @return: an IPeerToPeerProtocol
        @rtype: IPeerToPeerProtocol
        """
        raise NotImplementedError()
    
    def hasPeer(self, peer):
        raise NotImplementedError()
    
    def setConnectionsBetweenSuperPeerAndSimplePeers(self, superPeerAndSimplePeers):
        raise NotImplementedError()
    
    def getConnectionsBetweenSuperPeerAndSimplePeers(self):
        raise NotImplementedError()
    
    def setConnectionsBetweenSimplePeerAndSuperPeers(self, simplePeerAndSuperPeers):
        raise NotImplementedError()
    
    def getConnectionsBetweenSimplePeerAndSuperPeers(self):
        raise NotImplementedError()
    
    def setLinkAvailability(self, availability):
        raise NotImplementedError()
    
    def getLinkAvailability(self):
        raise NotImplementedError()
    
    def setSuperPeerLink(self, superPeerLink):
        raise NotImplementedError()
    
    def getSuperPeerLink(self):
        raise NotImplementedError()