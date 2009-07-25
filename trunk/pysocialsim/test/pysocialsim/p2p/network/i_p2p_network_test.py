from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
import unittest

class IP2PNetworkTest(unittest.TestCase):
    
    def test_try_create_i_p2p_network(self):
        self.assertRaises(NotImplementedError, IP2PNetwork)