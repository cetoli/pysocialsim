"""
Defines the module with the unit test of IPeerToPeerTopology interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
import pymockobject

import unittest

class IPeerToPeerTopologyTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerTopology)
        
    def testTryInvokeCreateConnection(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().addEdge, "1", "5")
        
    def testTryInvokeRemoveConnection(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().removeEdge, "1", "5")
    
    def testTryInvokeSetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().setPeerToPeerNetwork, pymockobject.create(IPeerToPeerNetwork))
    
    def testTryInvokeGetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getPeerToPeerNetwork)
    
    def testTryInvokeGetEdge(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getEdge, "1", "2")
    
    def testTryInvokeGetEdges(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getEdges, "1")
        
    def testTryInvokeCountEdges(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().countEdges, "1")
    
    def testTryInvokeAddNode(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().addNode, "1")
    
    def testTryInvokeRemoveNode(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().removeNode, "1")
        
    def testTryInvokeGetNode(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getNode, "1")
    
    def testTryInvokeGetNodes(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getNodes)    
    
    def testTryInvokeCountNodes(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().countNodes)
        
    def testTryInvokegetAdjacentNodes(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getAdjacentNodes, "1")
        
    def testTryInvokeHasNode(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().hasNode, "1")
        
    def testTryInvokeHasEdge(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().hasEdge, "1", "2")
        
    class PeerToPeerTopologyForTest(IPeerToPeerTopology):
        
        def __init__(self):
            pass