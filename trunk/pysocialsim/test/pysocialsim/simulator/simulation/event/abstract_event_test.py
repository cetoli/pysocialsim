from pysocialsim.simulator.simulation.event.abstract_event import AbstractEvent
import unittest

class AbstractEventTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEvent)