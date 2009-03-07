from pysocialsim.network.abstract_network_builder import AbstractNetworkBuilder
import unittest

class AbstractNetworkBuilderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractNetworkBuilder)