from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage
import unittest

class AbstractP2PMessageTest(unittest.TestCase):
    
    def test_try_create_abstract_p2p_message(self):
        self.assertRaises(NotImplementedError, AbstractP2PMessage)