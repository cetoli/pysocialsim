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
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().addEdge, 1, 5)
        
    def testTryInvokeRemoveConnection(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().removeEdge, 1, 5)
    
    def testTryInvokeSetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().setPeerToPeerNetwork, pymockobject.create(IPeerToPeerNetwork))
    
    def testTryInvokeGetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerTopologyForTest().getPeerToPeerNetwork)
        
    class PeerToPeerTopologyForTest(IPeerToPeerTopology):
        
        def __init__(self):
            pass