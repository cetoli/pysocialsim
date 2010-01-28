"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.context.social_network_member import SocialNetworkMember
from pysocialsim.common.p2p.peer.message.acknowledge_compose_social_network_peer_to_peer_message import AcknowledgeComposeSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.peer.message.create_social_network_peer_to_peer_message import CreateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.peer.message.update_social_network_peer_to_peer_message import UpdateSocialNetworkPeerToPeerMessage

class ComposeSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "COMPOSE_SOCIAL_NETWORK")
        
    def execute(self):
        message = self.getPeerToPeerMessage()
        peer = self.getPeer()
        if peer.isJoined():
            contextManager = peer.getContextManager()
            if message.hasParameter("opportunityId"):
                if contextManager.hasContext(IContext.OPPORTUNITY, message.getParameter("opportunityId")):
                    opportunity = contextManager.getContext(IContext.OPPORTUNITY, message.getParameter("opportunityId"))
                    socialNetwork = opportunity.getSocialNetwork()
                    
                    if socialNetwork.hasSocialNetworkMember(message.getSourceId()):
                        return
                    
                    member = SocialNetworkMember(message.getSourceId())
                    socialNetwork.addSocialNetworkMember(member)
                    if not socialNetwork.hasSocialNetworkMember(peer.getId()):
                        member = SocialNetworkMember(peer.getId())
                        socialNetwork.addSocialNetworkMember(member)
                    
                    opportunity.setVersion(opportunity.getVersion() + 1)
                    opportunityClone = opportunity.clone()
                    
                    if opportunity.getVersion() == 1:
                        if peer.countNeighbors() > 0:
                            neighbors = peer.getNeighbors()
                            for neighbor in neighbors:
                                createMessage = CreateSocialNetworkPeerToPeerMessage()
                                createMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), createMessage.getTime(), createMessage.getSize())
                                createMessage.registerParameter("opportunity", opportunityClone)
                                peer.send(createMessage)
                            
                    elif opportunity.getVersion() > 1:
                        if peer.countNeighbors() > 0:
                            neighbors = peer.getNeighbors()
                            for neighbor in neighbors:
                                updateMessage = UpdateSocialNetworkPeerToPeerMessage()
                                updateMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), updateMessage.getTime(), updateMessage.getSize())
                                updateMessage.registerParameter("opportunity", opportunityClone)
                                peer.send(updateMessage)
                    
                    ack_message = AcknowledgeComposeSocialNetworkPeerToPeerMessage()
                    ack_message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), message.getSourceId(), message.getTTL(), message.getPriority(), ack_message.getSize(), ack_message.getTime())
                    
                    
                    
                    ack_message.registerParameter("opportunity", opportunityClone)
                    
                    peer.send(ack_message)
                