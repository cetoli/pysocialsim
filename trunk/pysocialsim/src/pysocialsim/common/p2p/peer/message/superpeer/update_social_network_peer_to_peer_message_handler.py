"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.message.replicate_social_network_peer_to_peer_message import ReplicateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.topology.graph.i_node import INode
import math

class UpdateSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "UPDATE_SOCIAL_NETWORK")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            message = self.getPeerToPeerMessage()
            message.registerPeerId(peer.getId())
            if message.hasParameter("opportunity"):
                opportunity = message.getParameter("opportunity")
                
                socialNetwork = opportunity.getSocialNetwork()
                
                contextManager = peer.getContextManager()
                if not contextManager.hasContext(IContext.OPPORTUNITY, opportunity.getId()):
                    return
                
                actualOpportunity = contextManager.getContext(IContext.OPPORTUNITY, opportunity.getId())
                if opportunity.getVersion() < actualOpportunity.getVersion():
                    print "VERSAO ANTIGA"
                    return
                
                print "2B - SOCIAL NETWORK MEMBERS:", opportunity.getId(), opportunity.getSocialNetwork().countSocialNetworkMembers()
                
                contextManager.updateContext(IContext.OPPORTUNITY, opportunity)
                socialNetwork = opportunity.getSocialNetwork()
                
                neighborNumber = socialNetwork.countSocialNetworkMembers()
                if neighborNumber > 0:
                    minPercentage = 1.0
                    if (minPercentage * float(neighborNumber))  == 1:
                        return 
                    copyNumber = (minPercentage * neighborNumber) + math.log(opportunity.getVersion(), (minPercentage * neighborNumber))
                    
                    if round(copyNumber) >= 1:
                        neighbors = peer.getNeighbors()
                        for neighbor in neighbors:
                            
                            replicateMessage = ReplicateSocialNetworkPeerToPeerMessage()
                            replicateMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), 512, 0)
                            
                            replicateMessage.registerParameter("opportunity", opportunity)
                            
                            peer.send(replicateMessage)