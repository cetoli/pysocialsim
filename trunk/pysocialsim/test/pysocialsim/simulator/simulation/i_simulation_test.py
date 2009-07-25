from pysocialsim.simulator.simulation.i_simulation import ISimulation
import unittest

class ISimulationTest(unittest.TestCase):
    
    def test_try_create_i_simulation(self):
        self.assertRaises(NotImplementedError, ISimulation)