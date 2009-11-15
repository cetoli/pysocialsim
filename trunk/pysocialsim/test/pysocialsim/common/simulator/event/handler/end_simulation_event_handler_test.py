"""
Defines the module with the unit test of BeginSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pymockobject.events import ReturnValue
from pysocialsim.common.simulator.event.handler.end_simulation_event_handler import EndSimulationEventHandler
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
import pymockobject

import unittest

class BeginSimulationEventHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(EndSimulationEventHandler())
        handler = EndSimulationEventHandler()
        self.assertEquals("END_SIMULATION", handler.getHandle())
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        
    def testHandleSimulationEvent(self):
        handler = EndSimulationEventHandler()
        event = pymockobject.create(ISimulationEvent)
        event.getHandle.will(ReturnValue("END_SIMULATION"))
        self.assertEquals(event, handler.handleSimulationEvent(event))