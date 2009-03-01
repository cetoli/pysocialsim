from pysocialsim.simulator.abstract_simulator import AbstractSimulator
import unittest

class AbstractSimulatorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractSimulator)