"""
Defines the module with the unit test of NewSimplePeerSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 16/09/2009
"""
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event import NewSimplePeerSimulationEvent

import unittest

class NewSimplePeerSimulationEventTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSimplePeerSimulationEvent("1", 10))
        event = NewSimplePeerSimulationEvent("1", 10)
        self.assertEquals("NEW_SIMPLE_PEER", event.getHandle())
        self.assertEquals("1", event.getPeerId())
        self.assertEquals(10, event.getPriority())