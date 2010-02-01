'''
Created on 01/02/2010

@author: fabricio
'''
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.message.replicate_social_network_peer_to_peer_message import ReplicateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
import math

class ShareHardwarePeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "SHARE_HARDWARE")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            message = self.getPeerToPeerMessage()
            contextManager = peer.getContextManager()
            if not contextManager.hasContext(IContext.OPPORTUNITY, message.getParameter("opportunityId")):
                return 
            opportunity = contextManager.getParameter("opportunityId")
            socialNetwork = opportunity.getSocialNetwork()
            if not socialNetwork.hasSocialNetworkMember(message.getSourceId()):
                return
            member = socialNetwork.getSocialNetworkMember(message.getSourceId())
            hardwareSharing = message.getParameter("hardwareSharingContext")
            if member.hasHardwareSharing(hardwareSharing.getNodeDeviceType(), hardwareSharing.getId()):
                return
            member.registerHardwareSharing(hardwareSharing.getNodeDeviceType(), hardwareSharing)
            opportunity.setVersion(opportunity.getVersion() + 1)
            
            opportunityClone = opportunity.clone()
            
            neighborNumber = socialNetwork.countSocialNetworkMembers()
            if neighborNumber > 0:
                minPercentage = 0.25
                if (minPercentage * float(neighborNumber))  == 1:
                    return 
                copyNumber = (minPercentage * neighborNumber) + math.log(opportunity.getVersion(), (minPercentage * neighborNumber))
                
                if round(copyNumber) >= 1:
                    neighbors = peer.getNeighbors()
                    for neighbor in neighbors:
                        
                        replicateMessage = ReplicateSocialNetworkPeerToPeerMessage()
                        replicateMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), 512, 0)
                        
                        replicateMessage.registerParameter("opportunity", opportunityClone)
                        
                        peer.send(replicateMessage)