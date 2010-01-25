"""
Defines the module with the unit test of NewSimplePeerSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 16/09/2009
"""
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event import NewSuperPeerSimulationEvent

import unittest

class NewSuperPeerSimulationEventTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSuperPeerSimulationEvent("1", 10))
        event = NewSuperPeerSimulationEvent("1", 10)
        self.assertEquals("NEW_SUPER_PEER", event.getHandle())
        self.assertEquals("1", event.getPeerId())
        self.assertEquals(10, event.getPriority())