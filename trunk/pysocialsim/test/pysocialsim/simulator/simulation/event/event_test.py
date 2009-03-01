from pysocialsim.simulator.simulation.event.event import Event
import unittest

class EventTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Event)