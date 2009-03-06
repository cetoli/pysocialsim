from pysocialsim.network.peer.abstract_peer import AbstractPeer
import unittest

class AbstractPeerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractPeer)