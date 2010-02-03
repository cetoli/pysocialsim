'''
Created on 01/02/2010

@author: fabricio
'''
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.message.update_social_network_peer_to_peer_message import UpdateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator

class ShareHardwarePeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "SHARE_HARDWARE")
        
    def execute(self):
        peer = self.getPeer()
        if peer.isJoined():
            message = self.getPeerToPeerMessage()
            contextManager = peer.getContextManager()
            message.registerPeerId(peer.getId())
            
            if not contextManager.hasContext(IContext.OPPORTUNITY, message.getParameter("opportunityId")):
                return 
            
            
            
            opportunity = contextManager.getContext(IContext.OPPORTUNITY, message.getParameter("opportunityId"))
            
            
            socialNetwork = opportunity.getSocialNetwork()
            
            if not socialNetwork.hasSocialNetworkMember(message.getSourceId()):
                return
            
            member = socialNetwork.getSocialNetworkMember(message.getSourceId())
            hardwareSharing = message.getParameter("hardwareSharingContext")
            
            if member.hasHardwareSharing(hardwareSharing.getNodeDeviceType(), hardwareSharing.getId()):
                return
            
            if member.registerHardwareSharing(hardwareSharing.getNodeDeviceType(), hardwareSharing):
                print "OH POOOOOOOOOOOOOOOOOOOOOORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            
            opportunity.setVersion(opportunity.getVersion() + 1)
            
            
             
#            opportunityClone = opportunity.clone()
#            
#            replicateMessage = UpdateSocialNetworkPeerToPeerMessage()
#            replicateMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), peer.getId(), message.getTTL(), message.getPriority(), 512, 0)
#            
#            replicateMessage.registerParameter("opportunity", opportunityClone)
#            
#            dispatcher = peer.getPeerToPeerMessageDispatcher()
#            dispatcher.registerPeerToPeerMessage(replicateMessage)
#                        
#                    