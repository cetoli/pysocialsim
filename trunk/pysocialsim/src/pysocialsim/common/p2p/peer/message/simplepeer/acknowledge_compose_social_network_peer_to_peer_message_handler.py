"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.social_network_member import SocialNetworkMember
from pysocialsim.common.p2p.peer.context.i_context import IContext

class AcknowledgeComposeSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ACK_COMPOSE_SOCIAL_NETWORK")
    
    def execute(self):
        peer = self.getPeer()
        if peer.isJoined():
            message = self.getPeerToPeerMessage()
            if message.hasParameter("opportunity"):
                opportunity = message.getParameter("opportunity")
                socialNetwork = opportunity.getSocialNetwork()
                
                member = SocialNetworkMember(message.getSourceId())
                
                socialNetwork.addMember()
                
                contextManager = peer.getContextManager()
                
                contextManager.registerContext(IContext.OPPORTUNITY, opportunity)
                
                
                