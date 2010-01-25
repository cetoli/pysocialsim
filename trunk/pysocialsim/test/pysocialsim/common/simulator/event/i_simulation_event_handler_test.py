"""
Defines the module with the unit test of ISimulationEventHandler interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/08/2009
"""
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler

class ISimulationEventHandlerTest(unittest.TestCase):
    
    def testTryInstantiateInterface(self):
        self.assertRaises(NotImplementedError, ISimulationEventHandler)
        
    def testTryInvokeGetHandle(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().getHandle)
        
    def testTryInvokeGetSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().getSimulationEvent)
        
    def testTryInvokeHandleSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().handleSimulationEvent, pymockobject.create(ISimulationEvent))
        
    def testTryInvokeGetSimulation(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().getSimulation)
    
    def testTryInvokeInit(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().init, pymockobject.create(ISimulation))
        
    def testTryInvokeClone(self):
        self.assertRaises(NotImplementedError, self.ClassForTest().clone)
    
    class ClassForTest(ISimulationEventHandler):
        
        def __init__(self):
            pass