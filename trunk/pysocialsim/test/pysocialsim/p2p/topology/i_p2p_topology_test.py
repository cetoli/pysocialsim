from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
import unittest

class IP2PTopologyTest(unittest.TestCase):
    
    def test_try_create_i_p2p_topology_test(self):
        self.assertRaises(NotImplementedError, IP2PTopology)