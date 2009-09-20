"""
Defines the module with the specification of IPeerToPeerProtocol interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""

class IPeerToPeerProtocol(object):
    """
    Defines common operation for peer-to-peer protocols.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 20/09/2009
    """

    def __init__(self):
        raise NotImplementedError()
        
    def setPeerToPeerTopology(self, peerToPeerTopology):
        """
        Sets the peer-to-peer topology.
        @param peerToPeerTopology: an IPeerToPeerTopology
        @type peerToPeerTopology: IPeerToPeerTopology
        @return: an IPeerToPeerTopology
        @rtype: IPeerToPeerTopology
        """
        raise NotImplementedError()
    
    def getPeerToPeerTopology(self):
        """
        Gets the peer-to-peer topology.
        @return: an IPeerToPeerTopology
        @rtype: IPeerToPeerTopology
        """
        raise NotImplementedError()
    
    def join(self, peer):
        """
        Joins the peer in topology.
        @param peer: an IPeer
        @type peer: IPeer
        @return: If peer was joined in topology, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def leave(self, peer):
        """
        Leaves the peer in topology.
        @param peer: an IPeer
        @type peer: IPeer
        @return: If peer was leaved in topology, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    