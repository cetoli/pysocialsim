from pysocialsim.network.default_network import DefaultNetwork

class PureNetwork(DefaultNetwork):
    
    def __init__(self, topology):
        self.initialize(topology)