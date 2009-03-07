from pysocialsim.network.network_builder import NetworkBuilder
import unittest

class NetworkBuilderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, NetworkBuilder)