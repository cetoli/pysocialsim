"""
Defines the module with unit test of BeginSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.generator.begin_simulation_event import BeginSimulationEvent

import unittest

class BeginSimulationEventTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(BeginSimulationEvent())
        event = BeginSimulationEvent()
        self.assertEquals("BEGIN_SIMULATION", event.getHandle())
        self.assertEquals("", event.getPeerId())
        self.assertEquals(1, event.getPriority())