"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler

class ReplicateSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "REPLICATE_SOCIAL_NETWORK")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            return
        
        message = self.getPeerToPeerMessage()
        if not message.hasParameter("opportunity"):
            return
        
        opportunity = message.getParameter("opportunity")
        