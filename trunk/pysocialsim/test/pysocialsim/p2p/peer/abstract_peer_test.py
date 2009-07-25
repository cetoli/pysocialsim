from pysocialsim.p2p.peer.abstract_peer import AbstractPeer
import unittest

class AbstractPeerTest(unittest.TestCase):
    
    def test_try_create_abstract_peer(self):
        self.assertRaises(NotImplementedError, AbstractPeer)