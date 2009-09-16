"""
Defines the module with the specification of IPeerToPeerTopology interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/09/2009
"""

class IPeerToPeerTopology(object):
    """
    Defines the operations of peer-to-peer topology.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 15/09/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def createConnection(self, sourceId, targetId):
        """
        Creates a connection between two peers.
        @param sourceId: the identifier of source peer
        @type sourceId: int
        @param targetId: the identifier of target peer
        @type targetId: int
        @return: If connection was created, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def removeConnection(self, sourceId, targetId):
        """
        Removes a connection between two peers.
        @param sourceId: the identifier of source peer
        @type sourceId: int
        @param targetId: the identifier of target peer
        @type targetId: int
        @return: If connection was removed, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        """
        Sets the peer-to-peer network.
        @param peerToPeerNetwork: an IPeerToPeerNetwork
        @type peerToPeerNetwork: IPeerToPeerNetwork
        @return: an IPeerToPeerNetwork
        @rtype: IPeerToPeerNetwork
        """
        raise NotImplementedError()
    
    def getPeerToPeerNetwork(self):
        """
        Gets the peer-to-peer network.
        @return: an IPeerToPeerNetwork
        @rtype: IPeerToPeerNetwork
        """
        raise NotImplementedError()