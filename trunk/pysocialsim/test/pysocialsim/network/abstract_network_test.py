from pysocialsim.network.abstract_network import AbstractNetwork
import unittest

class AbstractNetworkTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractNetwork)