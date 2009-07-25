from pysocialsim.p2p.network.default_p2p_network_builder import DefaultP2PNetworkBuilder
from pysocialsim.base.interface import implements
from pysocialsim.p2p.network.i_p2p_network_builder import IP2PNetworkBuilder
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
import pymockobject
import unittest

class DefaultP2PNetworkBuilderTest(unittest.TestCase):
    
    def setUp(self):
        self.__builder = DefaultP2PNetworkBuilder()
    
    def test_implements_interface(self):
        self.assertTrue(implements(self.__builder, IP2PNetworkBuilder))
        
    def test_create_p2p_network(self):
        self.__builder.createP2PNetwork(pymockobject.create(IP2PTopology))
        network = self.__builder.getP2PNetwork()
        self.assertEquals(0, network.countPeers())
        
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, None)
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, 1)
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, False)
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, True)
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, "topology")
        self.assertRaises(TypeError, self.__builder.createP2PNetwork, 0.4)
    
    def test_build_p2p_network(self):
        self.__builder.createP2PNetwork(pymockobject.create(IP2PTopology))
        network = self.__builder.getP2PNetwork()
        self.assertEquals(0, network.countPeers())
        
        params = {"peers": 2000}
        params["protocol"] = {"module": "pysocialsim.p2p.protocol.gnutella_protocol",
                              "className": "GnutellaProtocol"}
                
        self.__builder.buildP2PNetwork(params)
        network = self.__builder.getP2PNetwork()
        self.assertEquals(2000, network.countPeers())
        
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, None)
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, 1)
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, True)
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, False)
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, "params")
        self.assertRaises(TypeError, self.__builder.buildP2PNetwork, 0.43)