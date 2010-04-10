"""
Defines the module with the unit test of BeginSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.handler.begin_simulation_event_handler import BeginSimulationEventHandler
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pymockobject.events import ReturnValue
import pymockobject

import unittest

class BeginSimulationEventHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(BeginSimulationEventHandler())
        handler = BeginSimulationEventHandler()
        self.assertEquals("BEGIN_SIMULATION", handler.getHandle())
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        
    def testHandleSimulationEvent(self):
        handler = BeginSimulationEventHandler()
        event = pymockobject.create(ISimulationEvent)
        event.getHandle.will(ReturnValue("BEGIN_SIMULATION"))
        self.assertEquals(event, handler.handleSimulationEvent(event))