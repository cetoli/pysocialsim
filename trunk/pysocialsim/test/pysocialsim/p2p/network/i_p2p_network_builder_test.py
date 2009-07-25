from pysocialsim.p2p.network.i_p2p_network_builder import IP2PNetworkBuilder
import unittest

class IP2PNetworkBuilderTest(unittest.TestCase):
    
    def test_try_create_i_p2p_network_builder_test(self):
        self.assertRaises(NotImplementedError, IP2PNetworkBuilder)