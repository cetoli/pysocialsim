"""
Defines the module with the implementation of SimplePeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.peer.message.simplepeer.advertise_opportunity_peer_to_peer_message_handler import AdvertiseOpportunityPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.message.simplepeer.compose_social_network_peer_to_peer_message_handler import ComposeSocialNetworkPeerToPeerMessageHandler

class SimplePeer(AbstractPeer):
    """
    Implements the basic functions of a peer.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self, id, peerToPeerNetwork):
        self.initialize(id, peerToPeerNetwork)
    
    def initialize(self, id, peerToPeerNetwork):
        AbstractPeer.initialize(self, IPeerToPeerNetwork.SIMPLE_PEER, id, peerToPeerNetwork)
        dispatcher = self.getPeerToPeerMessageDispatcher()
        dispatcher.registerPeerToPeerMessageHandler(AdvertiseOpportunityPeerToPeerMessageHandler())
        dispatcher.registerPeerToPeerMessageHandler(ComposeSocialNetworkPeerToPeerMessageHandler())
    
    @public
    def join(self):
        return AbstractPeer.join(self)

        