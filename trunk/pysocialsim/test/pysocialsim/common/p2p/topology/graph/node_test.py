"""
Defines the module with the unit test of Node class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pymockobject.events import ReturnValue
from pysocialsim.common.error import io_error
from pysocialsim.common.p2p.topology.graph.node import Node
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice
from pysocialsim.common.p2p.topology.graph.edge import Edge
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class NodeTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(Node("1", pymockobject.create(IPeerToPeerTopology)))
        node = Node("1", pymockobject.create(IPeerToPeerTopology))
        self.assertEquals(0, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertRaises(InvalidValueError, node.getNodeDevice, Node.PROCESSOR)
        self.assertRaises(InvalidValueError, node.getNodeDevice, Node.DISK)
        self.assertRaises(InvalidValueError, node.getNodeDevice, Node.NETWORK_ADAPTER)
        
        self.assertRaises(TypeError, Node, 1)
        self.assertRaises(TypeError, Node, "")
        self.assertRaises(TypeError, Node, 0.32)
        self.assertRaises(TypeError, Node, True)
        self.assertRaises(TypeError, Node, False)
    
    def testAddNodeDevices(self):
        node = Node("1", pymockobject.create(IPeerToPeerTopology))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.PROCESSOR))
        
        self.assertTrue(device, node.addNodeDevice(device))
        self.assertEquals(1, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.PROCESSOR))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.DISK))
        
        self.assertTrue(device, node.addNodeDevice(device))
        self.assertEquals(2, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.DISK))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        
        self.assertTrue(device, node.addNodeDevice(device))
        self.assertEquals(3, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.NETWORK_ADAPTER))
        
        self.assertRaises(TypeError, node.addNodeDevice, "")
        self.assertRaises(TypeError, node.addNodeDevice, 1)
        self.assertRaises(TypeError, node.addNodeDevice, 0.5)
        self.assertRaises(TypeError, node.addNodeDevice, True)
        self.assertRaises(TypeError, node.addNodeDevice, False)
        
        self.assertRaises(InvalidValueError, node.addNodeDevice, None)
    
    def testRemoveNodeDevices(self):
        node = Node("1", pymockobject.create(IPeerToPeerTopology))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.PROCESSOR))
        
        self.assertTrue(device, node.addNodeDevice(device))
        self.assertEquals(1, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.PROCESSOR))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.DISK))
        
        self.assertTrue(node.addNodeDevice(device))
        self.assertEquals(2, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.DISK))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        
        self.assertTrue(device, node.addNodeDevice(device))
        self.assertEquals(3, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        self.assertEquals(device, node.getNodeDevice(Node.NETWORK_ADAPTER))
        
        device = node.getNodeDevice(Node.DISK)
        self.assertTrue(node.removeNodeDevice(device))
        self.assertEquals(2, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        
        device = node.getNodeDevice(Node.PROCESSOR)
        self.assertTrue(node.removeNodeDevice(device))
        self.assertEquals(1, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        
        device = node.getNodeDevice(Node.NETWORK_ADAPTER)
        self.assertTrue(node.removeNodeDevice(device))
        self.assertEquals(0, node.countNodeDevices())
        self.assertTrue(node.getNodeDevices())
        
    def testInputData(self):
        node = Node("1", pymockobject.create(IPeerToPeerTopology))
        
        self.assertRaises(io_error.IOError, node.input, Node.DISK, "teste")
        self.assertRaises(io_error.IOError, node.input, Node.NETWORK_ADAPTER, "message")
        self.assertRaises(io_error.IOError, node.input, Node.PROCESSOR, "program")
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.PROCESSOR))
        device.input.expects("program").will(ReturnValue("program"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.DISK))
        device.input.expects("teste").will(ReturnValue("teste"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        device.input.expects("message").will(ReturnValue("message"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        self.assertEquals("teste", node.input(Node.DISK, "teste"))
        self.assertEquals("message", node.input(Node.NETWORK_ADAPTER, "message"))
        self.assertEquals("program", node.input(Node.PROCESSOR, "program"))
        
        self.assertRaises(TypeError, node.input, "DISK", "TESTE")
        self.assertRaises(TypeError, node.input, 1.0, "TESTE")
        self.assertRaises(InvalidValueError, node.input, None, "TESTE")

    def testOutputData(self):
        node = Node("1", pymockobject.create(IPeerToPeerTopology))
        
        self.assertRaises(io_error.IOError, node.output, Node.DISK, "teste")
        self.assertRaises(io_error.IOError, node.output, Node.NETWORK_ADAPTER, "message")
        self.assertRaises(io_error.IOError, node.output, Node.PROCESSOR, "program")
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.PROCESSOR))
        device.output.expects("program").will(ReturnValue("program"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.DISK))
        device.output.expects("teste").will(ReturnValue("teste"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        device = pymockobject.create(INodeDevice)
        device.getType.will(ReturnValue(Node.NETWORK_ADAPTER))
        device.output.expects("message").will(ReturnValue("message"))
        self.assertTrue(device, node.addNodeDevice(device))
        
        self.assertEquals("teste", node.output(Node.DISK, "teste"))
        self.assertEquals("message", node.output(Node.NETWORK_ADAPTER, "message"))
        self.assertEquals("program", node.output(Node.PROCESSOR, "program"))
        
        self.assertRaises(TypeError, node.output, "DISK", "TESTE")
        self.assertRaises(TypeError, node.output, 1.0, "TESTE")
        self.assertRaises(InvalidValueError, node.output, None, "TESTE")
        
    def testAddEdge(self):
        node1 = Node("12", pymockobject.create(IPeerToPeerTopology))
        node2 = Node("15", pymockobject.create(IPeerToPeerTopology))
        
        node1.setPeer(pymockobject.create(IPeer))
        node2.setPeer(pymockobject.create(IPeer))
        
        edge1 = Edge(node1, node2)
        self.assertTrue(node1.addEdge(edge1))
        self.assertEquals(1, node1.countEdges())
        self.assertEquals(edge1, node1.getEdge("15"))
        self.assertTrue(node1.getEdges())
        
        edge2 = Edge(node2, node1)
        self.assertTrue(node2.addEdge(edge2))
        self.assertEquals(1, node2.countEdges())
        self.assertEquals(edge2, node2.getEdge("12"))
        self.assertTrue(node2.getEdges())
        
        self.assertFalse(node1.addEdge(edge1))
        self.assertFalse(node1.addEdge(edge2))
        self.assertRaises(InvalidValueError, node1.getEdge, "12")
        
        self.assertFalse(node2.addEdge(edge2))
        self.assertFalse(node2.addEdge(edge1))
        self.assertRaises(InvalidValueError, node2.getEdge, "15")
        
        self.assertRaises(TypeError, node1.addEdge, 1)
        self.assertRaises(TypeError, node1.addEdge, 1.3)
        self.assertRaises(TypeError, node1.addEdge, True)
        self.assertRaises(TypeError, node1.addEdge, False)
        
    def testRemoveEdge(self):
        node1 = Node("12", pymockobject.create(IPeerToPeerTopology))
        node2 = Node("15", pymockobject.create(IPeerToPeerTopology))
        
        node1.setPeer(pymockobject.create(IPeer))
        node2.setPeer(pymockobject.create(IPeer))
        
        edge1 = Edge(node1, node2)
        self.assertTrue(node1.addEdge(edge1))
        self.assertEquals(1, node1.countEdges())
        self.assertEquals(edge1, node1.getEdge("15"))
        self.assertTrue(node1.getEdges())
        
        edge2 = Edge(node2, node1)
        self.assertTrue(node2.addEdge(edge2))
        self.assertEquals(1, node2.countEdges())
        self.assertEquals(edge2, node2.getEdge("12"))
        self.assertTrue(node2.getEdges())
        
        self.assertTrue(node1.removeEdge(edge1))
        self.assertEquals(0, node1.countEdges())
        self.assertRaises(InvalidValueError, node1.getEdge, "15")
        self.assertFalse(node1.removeEdge(edge1))
        
        self.assertTrue(node2.removeEdge(edge2))
        self.assertEquals(0, node2.countEdges())
        self.assertRaises(InvalidValueError, node2.getEdge, "12")
        self.assertFalse(node2.removeEdge(edge2))
        
        self.assertRaises(TypeError, node1.removeEdge, 1)
        self.assertRaises(TypeError, node1.removeEdge, 0.65)
        self.assertRaises(TypeError, node1.removeEdge, True)
        self.assertRaises(TypeError, node1.removeEdge, False)
        
        self.assertRaises(InvalidValueError, node1.removeEdge, None)
        self.assertRaises(InvalidValueError, node1.output, None, "TESTE")
