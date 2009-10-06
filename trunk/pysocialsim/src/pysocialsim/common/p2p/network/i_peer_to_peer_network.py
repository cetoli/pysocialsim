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