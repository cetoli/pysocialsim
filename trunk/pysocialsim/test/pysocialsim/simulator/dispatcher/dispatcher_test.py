from pysocialsim.simulator.dispatcher.dispatcher import Dispatcher
import unittest

class DispatcherTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Dispatcher)