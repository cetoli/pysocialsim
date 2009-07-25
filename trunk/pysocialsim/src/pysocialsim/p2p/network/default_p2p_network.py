from pysocialsim.p2p.network.abstract_p2p_network import AbstractP2PNetwork

class DefaultP2PNetwork(AbstractP2PNetwork):
    
    def __init__(self, topology):
        self.initialize(topology)