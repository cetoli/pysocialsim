from pysocialsim.simulator.simulation.stochastic.abstract_stochastic_simulation import AbstractStochasticSimulation
import unittest

class AbstractStochasticSimulationTest(unittest.TestCase):
    
    def test_try_create_abstract_stochastic_simulation(self):
        self.assertRaises(NotImplementedError, AbstractStochasticSimulation)