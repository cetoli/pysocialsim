"""
Defines the module with the implementation of SimplePeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class SimplePeer(AbstractPeer):
    """
    Implements the basic functions of a peer.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self, id):
        AbstractPeer.initialize(self, IPeerToPeerNetwork.SIMPLE_PEER, id)
        