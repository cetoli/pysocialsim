from pysocialsim.simulator.simulation.stochastic.i_stochastic_simulation import IStochasticSimulation
import unittest

class IStochasticSimulationTest(unittest.TestCase):
    
    def test_try_create_i_stochastic_simulation(self):
        self.assertRaises(NotImplementedError, IStochasticSimulation)