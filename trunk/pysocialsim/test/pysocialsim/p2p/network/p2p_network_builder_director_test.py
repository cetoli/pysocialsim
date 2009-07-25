from pysocialsim.p2p.network.default_p2p_network_builder import DefaultP2PNetworkBuilder
from pysocialsim.p2p.network.p2p_network_builder_director import P2PNetworkBuilderDirector
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
import pymockobject
import unittest

class P2PNetworkBuilderDirectorTest(unittest.TestCase):
    
    def test_build_default_p2p_network(self):
        builder = DefaultP2PNetworkBuilder()
        director = P2PNetworkBuilderDirector(builder)
        director.build("network.yaml", pymockobject.create(IP2PTopology))
        network = builder.getP2PNetwork()
        
        self.assertEquals(1000, network.countPeers())
        