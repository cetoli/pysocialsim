import unittest

from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler

class IEventHandlerTest(unittest.TestCase):
    
    def test_try_create_i_event_handler(self):
        self.assertRaises(NotImplementedError, IEventHandler)