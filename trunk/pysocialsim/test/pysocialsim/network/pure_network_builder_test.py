from pysocialsim.network.pure_network_builder import PureNetworkBuilder
from pysocialsim.network.topology.topology import Topology
import pymockobject
import unittest

class PureNetworkBuilderTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(PureNetworkBuilder())
        
        builder = PureNetworkBuilder()
        self.assertEquals(None, builder.getNetwork())
        
    def test_create_network(self):
        topology = pymockobject.create(Topology)
        builder = PureNetworkBuilder()
        
        self.assertTrue(builder.createNetwork(topology))
        self.assertTrue(builder.getNetwork())
        self.assertRaises(TypeError, builder.createNetwork, None)
        self.assertRaises(TypeError, builder.createNetwork, 1)
        self.assertRaises(TypeError, builder.createNetwork, False)
        self.assertRaises(TypeError, builder.createNetwork, True)
        self.assertRaises(TypeError, builder.createNetwork, "str")
        
    def test_build_network(self):
        topology = pymockobject.create(Topology)
        builder = PureNetworkBuilder()
        
        self.assertTrue(builder.createNetwork(topology))
        self.assertEquals(1000, builder.buildNetwork(peers=1000, min_permanence=21600, max_permanence=31104000, min_absence=3600, max_absence=2592000))
        self.assertTrue(builder.getNetwork())
        
        network = builder.getNetwork()
        
        self.assertEquals(1000, network.countPeers())
        
        