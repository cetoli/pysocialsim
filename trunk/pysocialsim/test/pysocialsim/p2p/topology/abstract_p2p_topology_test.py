from pysocialsim.p2p.topology.abstract_p2p_topology import AbstractP2PTopology
import unittest

class AbstractP2PTopologyTest(unittest.TestCase):
    
    def test_try_create_abstract_p2p_topology(self):
        self.assertRaises(NotImplementedError, AbstractP2PTopology)