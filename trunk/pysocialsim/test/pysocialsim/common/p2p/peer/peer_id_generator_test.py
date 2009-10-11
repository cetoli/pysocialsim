"""
Defines the module with the unit test implementation of PeerIdGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.peer.peer_id_generator import PeerIdGenerator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.error.invalid_value_error import InvalidValueError

import unittest

class PeerIdGeneratorTest(unittest.TestCase):
    
    def testGeneratePeerId(self):
        self.assertTrue(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER))
        self.assertEquals(57, len(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)))
        
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        self.assertTrue(id.index("superpeer") > 0)
    
        self.assertTrue(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertEquals(58, len(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER)))
        
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER)
        self.assertTrue(id.index("simplepeer") > 0)
        
        self.assertRaises(TypeError, PeerIdGenerator.generatePeerId, "0")
        self.assertRaises(TypeError, PeerIdGenerator.generatePeerId, 0.88)
        self.assertRaises(InvalidValueError, PeerIdGenerator.generatePeerId, -1)
        self.assertRaises(InvalidValueError, PeerIdGenerator.generatePeerId, 2)