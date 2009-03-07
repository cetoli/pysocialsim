from pysocialsim.network.peer.abstract_peer import AbstractPeer
from pysocialsim.network.peer.peer_constants import PeerConstants

class DefaultPeer(AbstractPeer):
    
    def __init__(self, id, network):
        self.initialize(id, network, PeerConstants.DEFAULT_PEER)