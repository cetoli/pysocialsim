"""
Defines the module with the unit test of AbstractSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/08/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pymockobject.events import ReturnValue
import pymockobject

import unittest

class AbstractSimulationEventHandlerTest(unittest.TestCase):
    
    def testTryInstantiateAbstractClass(self):
        self.assertRaises(NotImplementedError, AbstractSimulationEventHandler)
        
    def testGetterMethods(self):
        self.assertTrue(self.ClassForTest())
        
        handler = self.ClassForTest()
        
        self.assertEquals("TEST", handler.getHandle())
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        
    def testInitMethod(self):
        self.assertTrue(self.ClassForTest())
        
        handler = self.ClassForTest()
        simulation = pymockobject.create(ISimulation)
        
        handler.init(simulation)
        
        self.assertEquals(simulation, handler.getSimulation())
        
    def testTryInvokeHandleSimulationEvent(self):
        handler = self.ClassForTest()
        event = pymockobject.create(ISimulationEvent)
        event.getHandle.will(ReturnValue("TEST"))
        self.assertEquals(event, handler.handleSimulationEvent(event))
        
    def testCloneMethod(self):
        handler = self.ClassForTest()
        simulation = pymockobject.create(ISimulation)
        
        handler.init(simulation)
        
        self.assertTrue(handler.clone())
        
        clone = handler.clone()
        self.assertEquals(handler.getHandle(), clone.getHandle())
        self.assertEquals(handler.getSimulationEvent(), clone.getSimulationEvent())
        self.assertEquals(handler.getSimulation(), clone.getSimulation())
        
    class ClassForTest(AbstractSimulationEventHandler):
        
        def __init__(self):
            AbstractSimulationEventHandler.initialize(self, "TEST")
            