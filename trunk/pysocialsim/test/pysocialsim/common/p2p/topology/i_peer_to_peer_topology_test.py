"""
Defines the module with the unit test of IPeerToPeerTopology interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology

import unittest

class IPeerToPeerTopologyTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerTopology)