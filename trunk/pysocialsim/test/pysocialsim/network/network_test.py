from pysocialsim.network.network import Network
import unittest

class NetworkTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Network)