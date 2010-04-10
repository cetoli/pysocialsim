"""
Defines the module with the unit test of INodeDevice interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 19/09/2009
"""
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice

import unittest

class INodeDeviceTest(unittest.TestCase):
    
    def testTryCreateInstane(self):
        self.assertRaises(NotImplementedError, INodeDevice)
        
    def testInvokeGetType(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getType)
    
    def testInvokeGetCapacity(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getCapacity)
        
    def testInvokeGetFreeCapacity(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getFreeCapacity)
        
    def testInvokeGetInputSpeed(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getInputSpeed)
    
    def testInvokeGetOutputSpeed(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getOutputSpeed)
        
    def testInvokeGetUsedCapacity(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().getUsedCapacity)
        
    def testInput(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().input, "data")
        
    def testOutput(self):
        self.assertRaises(NotImplementedError, self.NodeDeviceTest().output, "data")
        
    class NodeDeviceTest(INodeDevice):
        
        def __init__(self):
            pass