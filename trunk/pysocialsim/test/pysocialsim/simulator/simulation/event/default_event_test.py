from pysocialsim.network.peer.peer import Peer
from pysocialsim.simulator.simulation.event.default_event import DefaultEvent
import pymockobject
import unittest

class DefaultEventTest(unittest.TestCase):
    
    def test_create_instance(self):
        peer = pymockobject.create(Peer)
        self.assertTrue(DefaultEvent(peer))
        
        event = DefaultEvent(peer)
        self.assertEquals("DEFAULT", event.getHandle())
        self.assertEquals(peer, event.getPeer())
        
        self.assertRaises(TypeError, DefaultEvent, None)
        self.assertRaises(TypeError, DefaultEvent, "test")
        self.assertRaises(TypeError, DefaultEvent, True)
        self.assertRaises(TypeError, DefaultEvent, False)
        self.assertRaises(TypeError, DefaultEvent, 1)
        self.assertRaises(TypeError, DefaultEvent, 0.56)