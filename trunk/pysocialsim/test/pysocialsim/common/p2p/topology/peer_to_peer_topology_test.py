"""
Defines the module with unit test of PeerToPeerTopology class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/10/2009
"""
from pysocialsim.common.p2p.topology.peer_to_peer_topology import PeerToPeerTopology
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class PeerToPeerTopologyTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(PeerToPeerTopology())
        
        topology = PeerToPeerTopology()
        self.assertFalse(topology.getPeerToPeerNetwork())
        self.assertEquals(0, topology.countNodes())
        
    def testSetPeerToPeerNetwork(self):
        topology = PeerToPeerTopology()
        network = pymockobject.create(IPeerToPeerNetwork)
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        self.assertEquals(network, topology.getPeerToPeerNetwork())
        
    def testAddNode(self):
        topology = PeerToPeerTopology()
        
        self.assertTrue(topology.addNode("1"))
        self.assertTrue(topology.hasNode("1"))
        self.assertEquals(1, topology.countNodes())
        self.assertTrue(topology.getNodes())
        self.assertTrue(topology.getNode("1"))
        node = topology.getNode("1")
        self.assertEquals("1", node.getId())
        
        self.assertTrue(topology.addNode("100"))
        self.assertTrue(topology.hasNode("100"))
        self.assertEquals(2, topology.countNodes())
        self.assertTrue(topology.getNodes())
        self.assertTrue(topology.getNode("100"))
        node = topology.getNode("100")
        self.assertEquals("100", node.getId())
        
        self.assertFalse(topology.addNode("1"))
        self.assertEquals(2, topology.countNodes())
        
        self.assertFalse(topology.addNode("100"))
        self.assertEquals(2, topology.countNodes())
        
        self.assertRaises(TypeError, topology.getNode, 12.0)
        
        self.assertRaises(InvalidValueError, topology.getNode, "-1")
        self.assertRaises(InvalidValueError, topology.getNode, None)
        self.assertRaises(InvalidValueError, topology.getNode, "500")
        
    def testRemoveNode(self):
        topology = PeerToPeerTopology()
        
        self.assertTrue(topology.addNode("1"))
        self.assertEquals(1, topology.countNodes())
        self.assertTrue(topology.getNodes())
        self.assertTrue(topology.getNode("1"))
        node = topology.getNode("1")
        self.assertEquals("1", node.getId())
        
        self.assertTrue(topology.addNode("100"))
        self.assertEquals(2, topology.countNodes())
        self.assertTrue(topology.getNodes())
        self.assertTrue(topology.getNode("100"))
        node = topology.getNode("100")
        self.assertEquals("100", node.getId())
        
        self.assertTrue(topology.removeNode("1"))
        self.assertEquals(1, topology.countNodes())
        self.assertRaises(InvalidValueError, topology.getNode, "1")
        self.assertFalse(topology.removeNode("1"))
        
        self.assertTrue(topology.removeNode("100"))
        self.assertEquals(0, topology.countNodes())
        self.assertRaises(InvalidValueError, topology.getNode, "100")
        self.assertFalse(topology.removeNode("100"))
        
    def testAddEdge(self):
        topology = PeerToPeerTopology()
        
        self.assertTrue(topology.addNode("1"))
        self.assertTrue(topology.hasNode("1"))
        topology.getNode("1").setPeer(pymockobject.create(IPeer))
        self.assertEquals(1, topology.countNodes())
        self.assertTrue(topology.addNode("2"))
        self.assertTrue(topology.hasNode("2"))
        topology.getNode("2").setPeer(pymockobject.create(IPeer))
        self.assertEquals(2, topology.countNodes())
        self.assertTrue(topology.addNode("3"))
        self.assertTrue(topology.hasNode("3"))
        topology.getNode("3").setPeer(pymockobject.create(IPeer))
        self.assertEquals(3, topology.countNodes())
        
        self.assertTrue(topology.addEdge("1", "2"))
        self.assertTrue(topology.hasEdge("1", "2"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertTrue(topology.getEdges("1"))
        self.assertTrue(topology.getNode("2") in topology.getAdjacentNodes("1"))
        self.assertEquals(0, topology.countEdges("2"))
        self.assertTrue(topology.getEdges("2"))
        edge = topology.getEdge("1", "2")
        self.assertEquals("2", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("2", "1"))
        self.assertTrue(topology.hasEdge("2", "1"))
        self.assertEquals(1, topology.countEdges("2"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertTrue(topology.getNode("1") in topology.getAdjacentNodes("2"))
        edge = topology.getEdge("2", "1")
        self.assertEquals("1", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("1", "3"))
        self.assertTrue(topology.hasEdge("1", "3"))
        self.assertEquals(2, topology.countEdges("1"))
        self.assertEquals(0, topology.countEdges("3"))
        self.assertTrue(topology.getNode("3") in topology.getAdjacentNodes("1"))
        edge = topology.getEdge("1", "3")
        self.assertEquals("3", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("3", "1"))
        self.assertTrue(topology.hasEdge("3", "1"))
        self.assertEquals(1, topology.countEdges("3"))
        self.assertEquals(2, topology.countEdges("1"))
        self.assertTrue(topology.getNode("1") in topology.getAdjacentNodes("3"))
        edge = topology.getEdge("3", "1")
        self.assertEquals("1", edge.getTargetNode().getId())
        
    def testRemoveEdge(self):
        topology = PeerToPeerTopology()
        
        self.assertTrue(topology.addNode("1"))
        topology.getNode("1").setPeer(pymockobject.create(IPeer))
        self.assertEquals(1, topology.countNodes())
        self.assertTrue(topology.addNode("2"))
        topology.getNode("2").setPeer(pymockobject.create(IPeer))
        self.assertEquals(2, topology.countNodes())
        self.assertTrue(topology.addNode("3"))
        topology.getNode("3").setPeer(pymockobject.create(IPeer))
        self.assertEquals(3, topology.countNodes())
        
        self.assertTrue(topology.addEdge("1", "2"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertTrue(topology.getEdges("1"))
        self.assertTrue(topology.getNode("2") in topology.getAdjacentNodes("1"))
        self.assertEquals(0, topology.countEdges("2"))
        self.assertTrue(topology.getEdges("2"))
        edge = topology.getEdge("1", "2")
        self.assertEquals("2", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("2", "1"))
        self.assertEquals(1, topology.countEdges("2"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertTrue(topology.getNode("1") in topology.getAdjacentNodes("2"))
        edge = topology.getEdge("2", "1")
        self.assertEquals("1", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("1", "3"))
        self.assertEquals(2, topology.countEdges("1"))
        self.assertEquals(0, topology.countEdges("3"))
        self.assertTrue(topology.getNode("3") in topology.getAdjacentNodes("1"))
        edge = topology.getEdge("1", "3")
        self.assertEquals("3", edge.getTargetNode().getId())
        
        self.assertTrue(topology.addEdge("3", "1"))
        self.assertEquals(1, topology.countEdges("3"))
        self.assertEquals(2, topology.countEdges("1"))
        self.assertTrue(topology.getNode("1") in topology.getAdjacentNodes("3"))
        edge = topology.getEdge("3", "1")
        self.assertEquals("1", edge.getTargetNode().getId())
        
        self.assertTrue(topology.removeEdge("1", "2"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertEquals(1, topology.countEdges("2")) 
        
        self.assertTrue(topology.removeEdge("2", "1"))
        self.assertEquals(1, topology.countEdges("1"))
        self.assertEquals(0, topology.countEdges("2"))
        
        self.assertTrue(topology.removeEdge("1", "3"))
        self.assertEquals(0, topology.countEdges("1"))
        self.assertEquals(1, topology.countEdges("3"))
        
        self.assertTrue(topology.removeEdge("3", "1"))
        self.assertEquals(0, topology.countEdges("1"))
        self.assertEquals(0, topology.countEdges("3"))