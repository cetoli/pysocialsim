"""
Defines the module with the implementation of PeerToPeerNetwork class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.network.abstract_peer_to_peer_network import AbstractPeerToPeerNetwork

class PeerToPeerNetwork(AbstractPeerToPeerNetwork):
    """
    classdocs
    """

    def __init__(self, simulation):
        AbstractPeerToPeerNetwork.initialize(self, simulation)
        