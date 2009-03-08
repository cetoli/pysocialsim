from pysocialsim.network.peer.peer import Peer
from pysocialsim.simulator.simulation.event.default_event import DefaultEvent
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulation.event.event import Event
import pymockobject
import unittest

class DefaultEventTest(unittest.TestCase):
    
    def test_create_instance(self):
        peer = pymockobject.create(Peer)
        self.assertTrue(DefaultEvent(peer, 1.0))
        
        event = DefaultEvent(peer, 5.0)
        self.assertEquals("DEFAULT", event.getHandle())
        self.assertEquals(peer, event.getPeer())
        self.assertEquals(5, event.getPriority())
        
        self.assertRaises(TypeError, DefaultEvent, None)
        self.assertRaises(TypeError, DefaultEvent, "test")
        self.assertRaises(TypeError, DefaultEvent, True)
        self.assertRaises(TypeError, DefaultEvent, False)
        self.assertRaises(TypeError, DefaultEvent, 1)
        self.assertRaises(TypeError, DefaultEvent, 0.56)
        
        self.assertTrue(implements(DefaultEvent(peer, 5.0), Event))