"""
Defines the module with unit test of AbstractPeerToPeerProtocol.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/10/2009
"""
from pysocialsim.common.p2p.protocol.abstract_peer_to_peer_protocol import AbstractPeerToPeerProtocol

import unittest

class AbstractPeerToPeerProtocolTest(unittest.TestCase):
    
    def testTryCreateClassInstance(self):
        self.assertRaises(NotImplementedError, AbstractPeerToPeerProtocol)
        
    def testInitializeProtocol(self):
        self.assertTrue(self.PeerToPeerProtocolForTest())
        
        protocol = self.PeerToPeerProtocolForTest()
        
        self.assertEquals(0, protocol.getPingHops())
        self.assertEquals(0, protocol.getPongHops())
        self.assertEquals(0, protocol.getPullHops())
        self.assertEquals(0, protocol.getPushHops())
        
        self.assertFalse(protocol.getPeerToPeerTopology())
        
    def testHopsConfiguration(self):
        protocol = self.PeerToPeerProtocolForTest()
        
        self.assertEquals(10, protocol.setPingHops(10))
        self.assertEquals(10, protocol.getPingHops())
        
        self.assertEquals(10, protocol.setPongHops(10))
        self.assertEquals(10, protocol.getPongHops())
        
        self.assertEquals(10, protocol.setPullHops(10))
        self.assertEquals(10, protocol.getPullHops())
        
        self.assertEquals(10, protocol.setPushHops(10))
        self.assertEquals(10, protocol.getPushHops())
        
    
        
    class PeerToPeerProtocolForTest(AbstractPeerToPeerProtocol):
        
        def __init__(self):
            AbstractPeerToPeerProtocol.initialize(self)