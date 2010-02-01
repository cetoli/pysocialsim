"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext

class ReplicateSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "REPLICATE_SOCIAL_NETWORK")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            return
        
        message = self.getPeerToPeerMessage()
        message.registerPeerId(peer.getId())
        if not message.hasParameter("opportunity"):
            return
        
        opportunity = message.getParameter("opportunity")
        contextManager = peer.getContextManager()
        
        if contextManager.hasContext(IContext.OPPORTUNITY, opportunity.getId()):
            actualOpportunity = contextManager.getContext(IContext.OPPORTUNITY, opportunity.getId())
            
            if opportunity.getVersion() > actualOpportunity.getVersion():
                contextManager.updateContext(IContext.OPPORTUNITY, opportunity)
        else:
            contextManager.registerContext(IContext.OPPORTUNITY, opportunity)
            
        print "OOOHH, YEEESSS", peer.getId()