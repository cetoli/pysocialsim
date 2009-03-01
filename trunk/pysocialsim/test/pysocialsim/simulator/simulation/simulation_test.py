from pysocialsim.simulator.simulation.simulation import Simulation
import unittest

class SimulationTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Simulation)