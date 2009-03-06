from pysocialsim.network.peer.abstract_peer import AbstractPeer

class DefaultPeer(AbstractPeer):
    
    def __init__(self, id, network):
        self.initialize(id, network)