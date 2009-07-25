import unittest

from pysocialsim.simulator.dispatcher.i_dispatcher import IDispatcher

class IDispatcherTest(unittest.TestCase):
    
    def test_try_create_i_dispatcher_test(self):
        self.assertRaises(NotImplementedError, IDispatcher)