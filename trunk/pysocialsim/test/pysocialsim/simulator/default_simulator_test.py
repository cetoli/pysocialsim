from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulator import Simulator
import pymockobject
import unittest

class DefaultSimulatorTest(unittest.TestCase):
    
    def test_create_instance(self):
        simulation = pymockobject.create(Simulation)
        self.assertTrue(DefaultSimulator(simulation))
        self.assertTrue(implements(DefaultSimulator(simulation), Simulator))