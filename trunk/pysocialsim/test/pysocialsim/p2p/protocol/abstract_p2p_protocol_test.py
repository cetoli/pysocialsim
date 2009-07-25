from pysocialsim.p2p.protocol.abstract_p2p_protocol import AbstractP2PProtocol
import unittest

class AbstractP2PProtocolTest(unittest.TestCase):
    
    def test_try_create_abstract_p2p_protocol_test(self):
        self.assertRaises(NotImplementedError, AbstractP2PProtocol)