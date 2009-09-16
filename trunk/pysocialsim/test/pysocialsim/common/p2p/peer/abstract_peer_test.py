"""
Defines the module with the unit test of AbstractPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

import unittest

class AbstractPeerTest(unittest.TestCase):
    
    def testTryCreateClassInstance(self):
        self.assertRaises(NotImplementedError, AbstractPeer)
        
    def testInitialization(self):
        self.assertTrue(self.PeerForTest(IPeerToPeerNetwork.SUPER_PEER, 1))
        superPeer = self.PeerForTest(IPeerToPeerNetwork.SUPER_PEER, 1)
        self.assertEquals(IPeerToPeerNetwork.SUPER_PEER, superPeer.getType())
        self.assertEquals(1, superPeer.getId())
        
        self.assertTrue(self.PeerForTest(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        peer = self.PeerForTest(IPeerToPeerNetwork.SIMPLE_PEER, 1)
        self.assertEquals(IPeerToPeerNetwork.SIMPLE_PEER, peer.getType())
        self.assertEquals(1, peer.getId())
        
    class PeerForTest(AbstractPeer):
        
        def __init__(self, type, id):
            AbstractPeer.initialize(self, type, id)