from pysocialsim.network.abstract_network_builder import AbstractNetworkBuilder
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.network.topology.topology import Topology
from pysocialsim.network.pure_network import PureNetwork
from pysocialsim.network.peer.default_peer import DefaultPeer

class PureNetworkBuilder(AbstractNetworkBuilder):
    
    def __init__(self):
        self.setNetwork(None)
    
    @public    
    def buildNetwork(self, **params):
        if not params.has_key("peers"):
            return 0
        peers = 0
        for id in range(params["peers"]):
            self.getNetwork().addPeer(DefaultPeer(id, self.getNetwork()))
            peers += 1
            
        return peers
    
    @public
    @require("topology", Topology)
    def createNetwork(self, topology):
        self.setNetwork(PureNetwork(topology))
        return self.getNetwork()
    
