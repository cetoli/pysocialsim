from pysocialsim.simulator.simulator import Simulator
import unittest

class SimulatorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Simulator)