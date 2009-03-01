from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulator import Simulator
from pysocialsim.simulator.dispatcher.dispatcher import Dispatcher
from pysocialsim.simulator.simulation.event.event import Event
from pymockobject.events import ReturnValue
import pymockobject
import unittest

class DefaultSimulatorTest(unittest.TestCase):
    
    def test_create_instance(self):
        simulation = pymockobject.create(Simulation)
        self.assertTrue(DefaultSimulator(simulation))
        self.assertTrue(implements(DefaultSimulator(simulation), Simulator))
        self.assertEquals(simulation, DefaultSimulator(simulation).getSimulation())
        
        self.assertRaises(TypeError, DefaultSimulator, None)
        self.assertRaises(TypeError, DefaultSimulator, "test")
        self.assertRaises(TypeError, DefaultSimulator, True)
        self.assertRaises(TypeError, DefaultSimulator, False)
        self.assertRaises(TypeError, DefaultSimulator, 1.9)
        self.assertRaises(TypeError, DefaultSimulator, 1)
    
    def test_set_dispatcher(self):
        simulation = pymockobject.create(Simulation)
        simulator = DefaultSimulator(simulation)
        dispatcher = pymockobject.create(Dispatcher)
        
        self.assertEquals(dispatcher, simulator.setDispatcher(dispatcher))
        
        self.assertRaises(TypeError, simulator.setDispatcher, None)
        self.assertRaises(TypeError, simulator.setDispatcher, 1)
        self.assertRaises(TypeError, simulator.setDispatcher, True)
        self.assertRaises(TypeError, simulator.setDispatcher, False)
        self.assertRaises(TypeError, simulator.setDispatcher, "Test")
    
    def test_handle_event(self):
        simulation = pymockobject.create(Simulation)
        simulator = DefaultSimulator(simulation)
        dispatcher = pymockobject.create(Dispatcher)
        event = pymockobject.create(Event)
        
        dispatcher.handleEvent.expects(event).will(ReturnValue(event))
        
        self.assertEquals(dispatcher, simulator.setDispatcher(dispatcher))        
        self.assertEquals(event, simulator.handleEvent(event))
        
        self.assertRaises(TypeError, simulator.handleEvent, None)
        self.assertRaises(TypeError, simulator.handleEvent, 123)
        self.assertRaises(TypeError, simulator.handleEvent, True)
        self.assertRaises(TypeError, simulator.handleEvent, False)
        self.assertRaises(TypeError, simulator.handleEvent, "test")
        self.assertRaises(TypeError, simulator.handleEvent, 0.88)   