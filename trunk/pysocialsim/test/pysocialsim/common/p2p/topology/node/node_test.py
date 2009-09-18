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
import pymockobject

import unittest

class NodeTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(Node(pymockobject.create(IPeerToPeerTopology)))
        node = Node(pymockobject.create(IPeerToPeerTopology))
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
        node = Node(pymockobject.create(IPeerToPeerTopology))
        
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
        node = Node(pymockobject.create(IPeerToPeerTopology))
        
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
        node = Node(pymockobject.create(IPeerToPeerTopology))
        
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
        node = Node(pymockobject.create(IPeerToPeerTopology))
        
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
          