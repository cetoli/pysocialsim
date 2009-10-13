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
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice
from pymockobject.events import ReturnValue
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.topology.graph.i_node import INode
import pymockobject

import unittest

class EdgeTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(Edge(Node("15", pymockobject.create(IPeerToPeerTopology)), pymockobject.create(INode)))
        
        node = Node("15", pymockobject.create(IPeerToPeerTopology))
        targetNode = pymockobject.create(INode)
        edge = Edge(node, targetNode)
        
        self.assertEquals(targetNode, edge.getTargetNode())
        self.assertEquals("15", node.getId())
        self.assertEquals(node, edge.getNode())
        
    def testDispatchData(self):
        node = Node("15", pymockobject.create(IPeerToPeerTopology))
        networkAdapter = pymockobject.create(INodeDevice)
        networkAdapter.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        networkAdapter.output.expects("data").will(ReturnValue("data"))
        node.addNodeDevice(networkAdapter)
        
        edge = Edge(node, pymockobject.create(INode))
        self.assertEquals("data", edge.dispatchData("data"))
        
        node = Node("15", pymockobject.create(IPeerToPeerTopology))
        networkAdapter = pymockobject.create(INodeDevice)
        networkAdapter.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        networkAdapter.output.expects(1).will(ReturnValue(1))
        node.addNodeDevice(networkAdapter)
        
        edge = Edge(node, pymockobject.create(INode))
        self.assertEquals(1, edge.dispatchData(1))
        
        node = Node("15", pymockobject.create(IPeerToPeerTopology))
        networkAdapter = pymockobject.create(INodeDevice)
        networkAdapter.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        networkAdapter.output.expects(1.45).will(ReturnValue(1.45))
        node.addNodeDevice(networkAdapter)
        
        edge = Edge(node, pymockobject.create(INode))
        self.assertEquals(1.45, edge.dispatchData(1.45))
        
        self.assertRaises(InvalidValueError, edge.dispatchData, None)