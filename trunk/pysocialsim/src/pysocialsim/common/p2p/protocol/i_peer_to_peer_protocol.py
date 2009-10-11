"""
Defines the module with the specification of IPeerToPeerProtocol interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.p2p.message.i_peer_to_peer_message_creator import IPeerToPeerMessageCreator

class IPeerToPeerProtocol(IPeerToPeerMessageCreator):
    
    PING = "PING"
    
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
    
    def routePeerToPeerMessage(self, peerToPeerMessage):
        """
        Routes the message to target.
        @param peerToPeerMessage: 
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def sendPeerToPeerMessage(self, peerToPeerMessage):
        """
        Sends a peer-to-peer message to target peer.
        @param peerToPeerMessage: an IPeerToPeerMessage
        @type peerToPeerMessage: IPeerToPeerMessage
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def receivePeerToPeerMessage(self, peerToPeerMessage):
        """
        Receives a peer-to-peer message to target peer.
        @param peerToPeerMessage: an IPeerToPeerMessage
        @type peerToPeerMessage: IPeerToPeerMessage
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def pushPeerToPeerMessage(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    def pullPeerToPeerMessage(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    def pingPeerToPeerMessage(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    def pongPeerToPeerMessage(self, peer, peerToPeerMessage):
        raise NotImplementedError()