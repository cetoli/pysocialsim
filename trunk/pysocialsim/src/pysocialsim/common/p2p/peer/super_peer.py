"""
Defines the module with the implementation SuperPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class SuperPeer(AbstractPeer):
    """
    classdocs
    """

    def __init__(self, id, peerToPeerNetwork):
        AbstractPeer.initialize(self, IPeerToPeerNetwork.SUPER_PEER, id, peerToPeerNetwork)    
        