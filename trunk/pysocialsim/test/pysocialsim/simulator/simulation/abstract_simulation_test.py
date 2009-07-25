from pysocialsim.simulator.simulation.abstract_simulation import AbstractSimulation
import unittest

class AbstractSimulationTest(unittest.TestCase):
    
    def test_try_create_abstrct_simulation(self):
        self.assertRaises(NotImplementedError, AbstractSimulation)