from pysocialsim.network.network import Network
from pysocialsim.simulator.simulation.default_simulation import DefaultSimulation
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.simulator import Simulator
from pysocialsim.simulator.simulation.event.event import Event
from pymockobject.events import ReturnValue
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
        
        self.assertRaises(TypeError, simulation.setSimulator, None)
        self.assertRaises(TypeError, simulation.setSimulator, "teste")
        self.assertRaises(TypeError, simulation.setSimulator, 123)
        self.assertRaises(TypeError, simulation.setSimulator, True)
        self.assertRaises(TypeError, simulation.setSimulator, False)
        self.assertRaises(TypeError, simulation.setSimulator, 0.235)
        
    def test_register_and_unregister_events(self):
        network = pymockobject.create(Network)
        simulation = DefaultSimulation(network)
        
        self.assertEquals(0, simulation.countEvents())
        
        event = pymockobject.create(Event)
        event.getPriority.will(ReturnValue(5))
        self.assertEquals(event, simulation.registerEvent(event))
        self.assertEquals(1, simulation.countEvents())
        
        event = pymockobject.create(Event)
        event.getPriority.will(ReturnValue(0))
        self.assertEquals(event, simulation.registerEvent(event))
        self.assertEquals(2, simulation.countEvents())
        
        event = pymockobject.create(Event)
        event.getPriority.will(ReturnValue(1))
        self.assertEquals(event, simulation.registerEvent(event))
        self.assertEquals(3, simulation.countEvents())
        
        event = simulation.unregisterEvent()
        self.assertEquals(0, event.getPriority())
        self.assertEquals(2, simulation.countEvents())
        
        event = simulation.unregisterEvent()
        self.assertEquals(1, event.getPriority())
        self.assertEquals(1, simulation.countEvents())
        
        event = simulation.unregisterEvent()
        self.assertEquals(5, event.getPriority())
        self.assertEquals(0, simulation.countEvents())
        
        self.assertRaises(TypeError, simulation.registerEvent, None)
        self.assertRaises(TypeError, simulation.registerEvent, True)
        self.assertRaises(TypeError, simulation.registerEvent, False)
        self.assertRaises(TypeError, simulation.registerEvent, "test")
        self.assertRaises(TypeError, simulation.registerEvent, 1)
        self.assertRaises(TypeError, simulation.registerEvent, 1.5)
        
        