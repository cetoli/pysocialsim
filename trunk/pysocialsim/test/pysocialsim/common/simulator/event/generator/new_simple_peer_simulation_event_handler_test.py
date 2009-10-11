"""
Defines the module with the unit test of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.simulator.event.handler.new_simple_peer_simulation_event_handler import NewSimplePeerSimulationEventHandler
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event import NewSimplePeerSimulationEvent
import pymockobject

import unittest

class NewSimplePeerSimulationEventHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSimplePeerSimulationEventHandler())
        handler = NewSimplePeerSimulationEventHandler()
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        self.assertEquals("NEW_SIMPLE_PEER", handler.getHandle())
        
    def testHandleSimulationEvent(self):
        handler = NewSimplePeerSimulationEventHandler()
        simulation = pymockobject.create(ISimulation)
        simulationEvent = NewSimplePeerSimulationEvent("1", 10)
        
        handler.init(simulation)
        
        self.assertEquals(simulation, handler.getSimulation())
        self.assertEquals(simulationEvent, handler.handleSimulationEvent(simulationEvent))
        self.assertTrue(simulationEvent.isHandled())