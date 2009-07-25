import unittest

from pysocialsim.p2p.peer.i_peer import IPeer

class IPeerTest(unittest.TestCase):
    
    def test_try_create_i_peer(self):
        self.assertRaises(NotImplementedError, IPeer)