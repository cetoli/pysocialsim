"""
Defines the module with the unit test of IPeerToPeerProtocol interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class IPeerToPeerProtocolTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerProtocol)
        
    def testTryInvokeSetPeerToPeerTopology(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerProcolForTest().setPeerToPeerTopology, pymockobject.create(IPeerToPeerTopology))
    
    def testTryInvokeGetPeerToPeerTopology(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerProcolForTest().getPeerToPeerTopology)
        
    def testTryInvokeJoin(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerProcolForTest().join, pymockobject.create(IPeer))
        
    def testTryInvokeLeave(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerProcolForTest().leave, pymockobject.create(IPeer))    
        
    class PeerToPeerProcolForTest(IPeerToPeerProtocol):
        
        def __init__(self):
            pass