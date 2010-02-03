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
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.topology.graph.i_node import INode

class AdvertiseOpportunityPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ADVERTISE_OPPORTUNITY")
    
    def execute(self):
        message = self.getPeerToPeerMessage()
        peer = self.getPeer()
        message.registerPeerId(peer.getId())
        
        if peer.isJoined():  
            if not message.hasParameter("opportunity"):
                return
            
            if (float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0):
                return
            
            opportunity = message.getParameter("opportunity")
            
            contextManager = peer.getContextManager()
            
            if contextManager.hasContext(IContext.OPPORTUNITY, opportunity.getId()):
                return
            
            socialProfile = peer.getSocialProfile()
            
            for constraint in opportunity.getInterestConstraints():
                if constraint.satisfyInterest(socialProfile):
                    print peer.getId(), "BATEEEEEEEEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
                    msg = ComposeSocialNetworkPeerToPeerMessage()
                    msg.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), message.getSourceId(), message.getTTL(), message.getPriority(), msg.getSize(), 0)
                    msg.registerParameter("opportunityId", opportunity.getId())
                    peer.send(msg)
                    break