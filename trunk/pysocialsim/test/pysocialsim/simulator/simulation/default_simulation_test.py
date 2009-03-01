from pysocialsim.network.network import Network
from pysocialsim.simulator.simulation.default_simulation import DefaultSimulation
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.simulator import Simulator
import pymockobject
import unittest

class DefaultSimulationTest(unittest.TestCase):
    
    def test_create_instance(self):
        network = pymockobject.create(Network)
        self.assertTrue(DefaultSimulation(network))
        
        simulation = DefaultSimulation(network)
        
        self.assertEquals(network, simulation.getNetwork())
        
        self.assertRaises(TypeError, DefaultSimulation, None)
        self.assertRaises(TypeError, DefaultSimulation, "test")
        self.assertRaises(TypeError, DefaultSimulation, True)
        self.assertRaises(TypeError, DefaultSimulation, False)
        self.assertRaises(TypeError, DefaultSimulation, 1)
        self.assertRaises(TypeError, DefaultSimulation, 0.25)
        
        self.assertTrue(implements(DefaultSimulation(network), Simulation))
    
    def test_set_simulator(self):
        network = pymockobject.create(Network)
        simulator = pymockobject.create(Simulator)
        
        simulation = DefaultSimulation(network)
        
        self.assertEquals(simulator, simulation.setSimulator(simulator))