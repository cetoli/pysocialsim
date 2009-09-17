"""
Defines the module with the unit test of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.handler.new_super_peer_simulation_event_handler import NewSuperPeerSimulationEventHandler
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event import NewSuperPeerSimulationEvent
import pymockobject

import unittest

class NewSuperPeerSimulationEventHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSuperPeerSimulationEventHandler())
        handler = NewSuperPeerSimulationEventHandler()
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        self.assertEquals("NEW_SUPER_PEER", handler.getHandle())
        
    def testHandleSimulationEvent(self):
        handler = NewSuperPeerSimulationEventHandler()
        simulation = pymockobject.create(ISimulation)
        simulationEvent = NewSuperPeerSimulationEvent(1, 10)
        
        handler.init(simulation)
        
        self.assertEquals(simulation, handler.getSimulation())
        self.assertEquals(simulationEvent, handler.handleSimulationEvent(simulationEvent))
        self.assertTrue(simulationEvent.isHandled())