from pysocialsim.simulator.event.abstract_event import AbstractEvent
import unittest

class AbstractEventTest(unittest.TestCase):
    
    def test_try_create_abstract_event(self):
        self.assertRaises(NotImplementedError, AbstractEvent)