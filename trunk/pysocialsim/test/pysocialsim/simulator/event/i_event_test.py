from pysocialsim.simulator.event.i_event import IEvent
import unittest

class IEventTest(unittest.TestCase):
    
    def test_try_create_i_event(self):
        self.assertRaises(NotImplementedError, IEvent)