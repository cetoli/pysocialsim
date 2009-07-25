from pysocialsim.simulator.i_simulator import ISimulator
import unittest

class ISimulatorTest(unittest.TestCase):
    
    def test_try_create_i_simulator_test(self):
        self.assertRaises(NotImplementedError, ISimulator)