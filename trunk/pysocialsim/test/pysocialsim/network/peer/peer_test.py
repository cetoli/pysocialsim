from pysocialsim.network.peer.peer import Peer
import unittest

class PeerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Peer)