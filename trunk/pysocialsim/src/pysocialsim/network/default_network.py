from pysocialsim.network.abstract_network import AbstractNetwork

class DefaultNetwork(AbstractNetwork):
    
    def __init__(self, topology):
        self.initialize(topology)