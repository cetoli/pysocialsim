from pysocialsim.simulator.simulation.stochastic.i_stochastic_model import IStochasticModel
import unittest

class IStochasticModelTest(unittest.TestCase):
    
    def test_try_create_i_stochastic_model(self):
        self.assertRaises(NotImplementedError, IStochasticModel)