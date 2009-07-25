from pysocialsim.p2p.topology.default_p2p_topology import DefaultP2PTopology
from pysocialsim.base.interface import implements
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
import pymockobject
import unittest

class DefaultP2PTopologyTest(unittest.TestCase):
    
    def setUp(self):
        self.__topology = DefaultP2PTopology()
        
    def test_implements_interface(self):
        self.assertTrue(implements(self.__topology, IP2PTopology))
        
    def test_set_p2p_network(self):
        network = pymockobject.create(IP2PNetwork)
        
        self.assertEquals(network, self.__topology.setP2PNetwork(network))
        self.assertEquals(network, self.__topology.getP2PNetwork())
        
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, None)
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, True)
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, False)
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, 1)
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, 0.2)
        self.assertRaises(TypeError, self.__topology.setP2PNetwork, "network")
        
    def test_add_node(self):
        self.assertTrue(self.__topology.addNode(1))
        self.assertEquals(1, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.addNode(2))
        self.assertEquals(2, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.addNode(3))
        self.assertEquals(3, self.__topology.countNodes())
        
        self.assertRaises(StandardError, self.__topology.addNode, 1)
        self.assertEquals(3, self.__topology.countNodes())
        
        self.assertRaises(TypeError, self.__topology.addNode, None)
        self.assertRaises(TypeError, self.__topology.addNode, True)
        self.assertRaises(TypeError, self.__topology.addNode, False)
        self.assertRaises(TypeError, self.__topology.addNode, 0.34)
        self.assertRaises(TypeError, self.__topology.addNode, "1")
        
    def test_remove_node(self):
        self.assertTrue(self.__topology.addNode(1))
        self.assertEquals(1, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.addNode(2))
        self.assertEquals(2, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.addNode(3))
        self.assertEquals(3, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.removeNode(1))
        self.assertEquals(2, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.removeNode(3))
        self.assertEquals(1, self.__topology.countNodes())
        
        self.assertTrue(self.__topology.removeNode(2))
        self.assertEquals(0, self.__topology.countNodes())
        
        self.assertRaises(TypeError, self.__topology.removeNode, None)
        self.assertRaises(TypeError, self.__topology.removeNode, True)
        self.assertRaises(TypeError, self.__topology.removeNode, False)
        self.assertRaises(TypeError, self.__topology.removeNode, 0.34)
        self.assertRaises(TypeError, self.__topology.removeNode, "1")
        
    def test_create_connection(self):
        self.assertTrue(self.__topology.createConnection(1, 2))
        self.assertEquals(2, self.__topology.countNodes())
        self.assertTrue(self.__topology.isNeighbor(1, 2))
        self.assertTrue(self.__topology.isNeighbor(2, 1))
        self.assertEquals(1, self.__topology.countConnections())
        
        self.assertTrue(self.__topology.createConnection(1, 3))
        self.assertEquals(3, self.__topology.countNodes())
        self.assertTrue(self.__topology.isNeighbor(1, 3))
        self.assertTrue(self.__topology.isNeighbor(3, 1))
        self.assertEquals(2, self.__topology.countConnections())
    
        self.assertRaises(TypeError, self.__topology.createConnection, None, 2)
        self.assertRaises(TypeError, self.__topology.createConnection, 1, None)
        self.assertRaises(TypeError, self.__topology.createConnection, None, None)
        
        self.assertRaises(TypeError, self.__topology.createConnection, 2, True)
        self.assertRaises(TypeError, self.__topology.createConnection, True, 3)
        self.assertRaises(TypeError, self.__topology.createConnection, True, True)
        
        self.assertRaises(TypeError, self.__topology.createConnection, 2, False)
        self.assertRaises(TypeError, self.__topology.createConnection, False, 3)
        self.assertRaises(TypeError, self.__topology.createConnection, False, False)
        
        self.assertRaises(TypeError, self.__topology.createConnection, 2, 3.0)
        self.assertRaises(TypeError, self.__topology.createConnection, 2.0, 3)
        self.assertRaises(TypeError, self.__topology.createConnection, 2.0, 3.0)
        
        self.assertRaises(TypeError, self.__topology.createConnection, 2, "3")
        self.assertRaises(TypeError, self.__topology.createConnection, "2", 3)
        self.assertRaises(TypeError, self.__topology.createConnection, "2", "3")
        
        self.assertRaises(StandardError, self.__topology.createConnection, 1, 2)
        self.assertRaises(StandardError, self.__topology.createConnection, 1, 3)
        
    
    def  test_remove_connections(self):
        self.assertTrue(self.__topology.createConnection(1, 2))
        self.assertEquals(2, self.__topology.countNodes())
        self.assertTrue(self.__topology.isNeighbor(1, 2))
        self.assertTrue(self.__topology.isNeighbor(2, 1))
        self.assertEquals(1, self.__topology.countConnections())
        
        self.assertTrue(self.__topology.createConnection(1, 3))
        self.assertEquals(3, self.__topology.countNodes())
        self.assertTrue(self.__topology.isNeighbor(1, 3))
        self.assertTrue(self.__topology.isNeighbor(3, 1))
        self.assertEquals(2, self.__topology.countConnections())
        
        self.assertTrue(self.__topology.removeConnection(1, 2))
        self.assertEquals(3, self.__topology.countNodes())
        self.assertFalse(self.__topology.isNeighbor(1, 2))
        self.assertFalse(self.__topology.isNeighbor(2, 1))
        self.assertEquals(1, self.__topology.countConnections())
        
        self.assertTrue(self.__topology.removeConnection(1, 3))
        self.assertEquals(3, self.__topology.countNodes())
        self.assertFalse(self.__topology.isNeighbor(1, 3))
        self.assertFalse(self.__topology.isNeighbor(3, 1))
        self.assertEquals(0, self.__topology.countConnections())
        
        self.assertRaises(TypeError, self.__topology.removeConnection, None, 2)
        self.assertRaises(TypeError, self.__topology.removeConnection, 1, None)
        self.assertRaises(TypeError, self.__topology.removeConnection, None, None)
        
        self.assertRaises(TypeError, self.__topology.removeConnection, 1, True)
        self.assertRaises(TypeError, self.__topology.removeConnection, True, 2)
        self.assertRaises(TypeError, self.__topology.removeConnection, True, True)
        
        self.assertRaises(TypeError, self.__topology.removeConnection, 1, False)
        self.assertRaises(TypeError, self.__topology.removeConnection, False, 2)
        self.assertRaises(TypeError, self.__topology.removeConnection, False, False)
        
        self.assertRaises(TypeError, self.__topology.removeConnection, 1, 2.0)
        self.assertRaises(TypeError, self.__topology.removeConnection, 1.0, 2)
        self.assertRaises(TypeError, self.__topology.removeConnection, 1.0, 2.0)
        
        self.assertRaises(TypeError, self.__topology.removeConnection, 1, "2")
        self.assertRaises(TypeError, self.__topology.removeConnection, "1", 2)
        self.assertRaises(TypeError, self.__topology.removeConnection, "1", "2")
        
        self.assertRaises(StandardError, self.__topology.removeConnection, 1, 2)
        self.assertRaises(StandardError, self.__topology.removeConnection, 1, 3)