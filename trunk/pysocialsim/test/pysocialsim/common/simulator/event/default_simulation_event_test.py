"""
Defines the module with the o,plementation of DefaultSimulationEventTest class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.simulator.event.default_simulation_event import DefaultSimulationEvent
import pymockobject

import unittest

class DefaultSimulationEventTest(unittest.TestCase):
    
    def testCreateAnObject(self):
        event = DefaultSimulationEvent(12, 10)
        
        self.assertEquals("DEFAULT", event.getHandle())
        self.assertEquals(12, event.getPeerId())
        self.assertEquals(10, event.getPriority())
        self.assertFalse(event.isHandled())
        
    def testChangeStateOfEventToHandled(self):
        event = DefaultSimulationEvent(12, 10)
        
        self.assertFalse(event.isHandled())
        event.handled()
        self.assertTrue(event.isHandled())
        
    def testTryCreateAnObjectWithInvalidObjects(self):
        self.assertRaises(TypeError, DefaultSimulationEvent, "", 1)
        self.assertRaises(TypeError, DefaultSimulationEvent, pymockobject.create(IPeer), "")
        self.assertRaises(TypeError, DefaultSimulationEvent, "", "")
        

        self.assertRaises(TypeError, DefaultSimulationEvent, 0.55, 1)
        self.assertRaises(TypeError, DefaultSimulationEvent, pymockobject.create(IPeer), 0.56)
        self.assertRaises(TypeError, DefaultSimulationEvent, 0.1, 0.4)
        
    def testEquals(self):
        event1 = DefaultSimulationEvent(1, 10)
        event2 = DefaultSimulationEvent(1, 10)
        
        self.assertEquals(event1, event2)
        self.assertNotEquals(event1, None)