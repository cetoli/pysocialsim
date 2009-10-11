"""
Defines the module with unit test of BeginSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.generator.end_simulation_event import EndSimulationEvent
import unittest

class BeginSimulationEventTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(EndSimulationEvent(10))
        event = EndSimulationEvent(10)
        self.assertEquals("END_SIMULATION", event.getHandle())
        self.assertEquals("", event.getPeerId())
        self.assertEquals(10, event.getPriority())