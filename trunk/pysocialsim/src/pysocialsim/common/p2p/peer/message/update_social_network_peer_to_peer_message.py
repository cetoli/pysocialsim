"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage

class UpdateSocialNetworkPeerToPeerMessage(AbstractPeertoPeerMessage):
    
    def __init__(self):
        AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, "UPDATE_SOCIAL_NETWORK", 512*8)