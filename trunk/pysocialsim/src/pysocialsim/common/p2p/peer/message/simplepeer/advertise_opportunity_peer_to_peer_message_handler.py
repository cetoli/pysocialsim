"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.message.compose_social_network_peer_to_peer_message import ComposeSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator

class AdvertiseOpportunityPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ADVERTISE_OPPORTUNITY")
    
    def execute(self):
        message = self.getPeerToPeerMessage()
        peer = self.getPeer()
            
        opportunity = message.getParameter("opportunity")
        
        socialProfile = peer.getSocialProfile()
        
        for constraint in opportunity.getInterestConstraints():
            if constraint.satisfyInterest(socialProfile):
                print peer.getId(), "BATEEEEEEEEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
                msg = ComposeSocialNetworkPeerToPeerMessage()
                msg.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), message.getSourceId(), message.getTTL(), message.getPriority(), msg.getSize(), 0)
                msg.registerParameter("opportunityId", opportunity.getId())
                msg.registerParameter("socialProfile", socialProfile)
                peer.send(msg)
                break