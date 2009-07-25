from pysocialsim.p2p.network.abstract_p2p_network import AbstractP2PNetwork
import unittest

class AbstractP2PNetworkTest(unittest.TestCase):
    
    def test_try_create_abstract_p2p_network_test(self):
        self.assertRaises(NotImplementedError, AbstractP2PNetwork)