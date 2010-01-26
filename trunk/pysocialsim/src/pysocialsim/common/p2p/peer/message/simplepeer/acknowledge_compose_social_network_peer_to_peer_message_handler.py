"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler

class AcknowledgeComposeSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ACK_COMPOSE_SOCIAL_NETWORK")
    
    def execute(self):
        print "CAAAAAAAAAAAAAAAAAGUEEEEEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIIIIIIIII"