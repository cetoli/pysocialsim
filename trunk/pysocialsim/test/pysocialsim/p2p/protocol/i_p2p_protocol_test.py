import unittest

from pysocialsim.p2p.protocol.i_p2p_protocol import IP2PProtocol

class IP2PProtocolTest(unittest.TestCase):
    
    def test_try_create_i_p2p_protocol(self):
        self.assertRaises(NotImplementedError, IP2PProtocol)