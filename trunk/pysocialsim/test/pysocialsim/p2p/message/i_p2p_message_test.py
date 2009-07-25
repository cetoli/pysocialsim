from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
import unittest

class IP2PMessageTest(unittest.TestCase):
    
    def test_try_create_i_p2p_message(self):
        self.assertRaises(NotImplementedError, IP2PMessage)