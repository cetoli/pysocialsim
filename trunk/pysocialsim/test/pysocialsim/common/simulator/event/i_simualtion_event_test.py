"""
Defines the module with the implementation of ISimulationEventTest.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent

import unittest

class ISimulationEventTest(unittest.TestCase):
    
    def testTryInstantiateInterface(self):
        self.assertRaises(NotImplementedError, ISimulationEvent)
        
    def testTryInvokeGetHandle(self):
        event = self.SimulationEventForTest()
        self.assertRaises(NotImplementedError, event.getHandle)
        
    def testTryInvokeGetPeer(self):
        event = self.SimulationEventForTest()
        self.assertRaises(NotImplementedError, event.getPeerId)
        
    def testTryInvokeGetPriority(self):
        event = self.SimulationEventForTest()
        self.assertRaises(NotImplementedError, event.getPriority)
        
    def testTryInvokeHandled(self):
        event = self.SimulationEventForTest()
        self.assertRaises(NotImplementedError, event.handled)
    
    def testTryInvokeIsHandled(self):
        event = self.SimulationEventForTest()
        self.assertRaises(NotImplementedError, event.isHandled)
        
    class SimulationEventForTest(ISimulationEvent):
        
        def __init__(self):
            pass