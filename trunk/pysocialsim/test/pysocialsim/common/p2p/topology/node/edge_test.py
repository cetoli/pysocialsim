"""
Defines the module with the unit test of Edge class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""
from pysocialsim.common.p2p.topology.graph.edge import Edge
from pysocialsim.common.p2p.topology.graph.node import Node
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
import pymockobject

import unittest

class EdgeTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(Edge(Node(15, pymockobject.create(IPeerToPeerTopology))))
        
        node = Node(15, pymockobject.create(IPeerToPeerTopology))
        edge = Edge(node)
        
        self.assertEquals(node, edge.getTargetNode())