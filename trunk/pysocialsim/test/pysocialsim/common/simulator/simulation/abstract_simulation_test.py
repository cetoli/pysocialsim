"""
Defines the module with the unit test of AbstractSimulation class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.simulator.simulation.abstract_simulation import AbstractSimulation
from pysocialsim.common.simulator.default_simulator import DefaultSimulator
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pymockobject.events import ReturnValue
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.error.register_simulation_event_error import RegisterSimulationEventError
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.error.unregister_simulation_event_error import UnregisterSimulationEventError
from random import randint
from pysocialsim.common.simulator.i_simulator import ISimulator
import pymockobject

import unittest

class AbstractSimulationTest(unittest.TestCase):
    
    def testTryCreateAbstractClassInstance(self):
        self.assertRaises(NotImplementedError, AbstractSimulation)
    
    def testExecute(self):
        simulator = DefaultSimulator()
        
        simulation = self.SimulationForTest()
        self.assertEquals(10, simulation.setSimulationTime(10))
        self.assertEquals(simulator, simulation.setSimulator(simulator))
        
        peerToPeerNetwork = pymockobject.create(IPeerToPeerNetwork)
        peerToPeerNetwork.setSimulation.expects(simulation).will(ReturnValue(simulation))
        
        self.assertEquals(peerToPeerNetwork, simulation.setPeerToPeerNetwork(peerToPeerNetwork))
        
        generator1 = self.SimulationEventGeneratorForTest(1000)
        self.assertEquals(generator1, simulation.addSimulationEventGenerator(generator1))
        self.assertEquals(1, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        generator2 = self.SimulationEventGeneratorForTest(2000)
        self.assertEquals(generator2, simulation.addSimulationEventGenerator(generator2))
        self.assertEquals(2, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        self.assertEquals(3000, simulation.configure())
        
        simulation.execute()
        self.assertEquals(0, simulation.countSimulationEventQueues())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        
        simulation.configure()
        self.assertEquals(3, simulation.countSimulationEventQueues())
        
    def testSetAndGetSimulator(self):
        simulator = DefaultSimulator()
        simulation = self.SimulationForTest()
        
        self.assertEquals(simulator, simulation.setSimulator(simulator))
        self.assertEquals(simulator, simulation.getSimulator())
        
        self.assertRaises(TypeError, simulation.setSimulator, 1)
        self.assertRaises(TypeError, simulation.setSimulator, "")
        self.assertRaises(TypeError, simulation.setSimulator, 0.444)
        self.assertRaises(TypeError, simulation.setSimulator, True)
        self.assertRaises(TypeError, simulation.setSimulator, False)
        
        self.assertRaises(InvalidValueError, simulation.setSimulator, None)
        
    def testRegisterSimulationEvent(self):
        simulator = DefaultSimulator()
        
        simulation = self.SimulationForTest()
        self.assertEquals(simulator, simulation.setSimulator(simulator))
        
        simulation.execute()
        self.assertEquals(0, simulation.countSimulationEventQueues())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        
        simulation.configure()
        self.assertEquals(3, simulation.countSimulationEventQueues())
        
        simulationEvent1 = pymockobject.create(ISimulationEvent)
        simulationEvent1.getHandle.will(ReturnValue("CONNECT"))
        simulationEvent1.getPriority.will(ReturnValue(1))
        
        self.assertEquals(simulationEvent1, simulation.registerSimulationEvent(simulationEvent1))
        self.assertEquals(1, simulation.countSimulationEvents("CONNECT"))
        self.assertEquals(simulationEvent1, simulation.getSimulationEvent("CONNECT"))
        
        simulationEvent2 = pymockobject.create(ISimulationEvent)
        simulationEvent2.getHandle.will(ReturnValue("DISCONNECT"))
        simulationEvent2.getPriority.will(ReturnValue(1))
        
        self.assertEquals(simulationEvent2, simulation.registerSimulationEvent(simulationEvent2))
        self.assertEquals(1, simulation.countSimulationEvents("DISCONNECT"))
        self.assertEquals(simulationEvent2, simulation.getSimulationEvent("DISCONNECT"))
        
        simulationEvent3 = pymockobject.create(ISimulationEvent)
        simulationEvent3.getHandle.will(ReturnValue("ADVERTISE"))
        simulationEvent3.getPriority.will(ReturnValue(1))
        
        self.assertEquals(simulationEvent3, simulation.registerSimulationEvent(simulationEvent3))
        self.assertEquals(1, simulation.countSimulationEvents("ADVERTISE"))
        self.assertEquals(simulationEvent3, simulation.getSimulationEvent("ADVERTISE"))
        
        simulationEvent4 = pymockobject.create(ISimulationEvent)
        simulationEvent4.getHandle.will(ReturnValue("TEST"))
    
        self.assertRaises(RegisterSimulationEventError, simulation.registerSimulationEvent, simulationEvent4)
        self.assertRaises(InvalidValueError, simulation.registerSimulationEvent, None)
        self.assertRaises(InvalidValueError, simulation.getSimulationEvent, "TEST")
        
        self.assertRaises(TypeError, simulation.registerSimulationEvent, 1)
        self.assertRaises(TypeError, simulation.registerSimulationEvent, "ddd")
        self.assertRaises(TypeError, simulation.registerSimulationEvent, 1.8)
        self.assertRaises(TypeError, simulation.registerSimulationEvent, True)
        self.assertRaises(TypeError, simulation.registerSimulationEvent, False)
    
    def testUnregisterSimulationEvent(self):
        simulator = DefaultSimulator()
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        
        simulation = self.SimulationForTest()
        self.assertEquals(simulator, simulation.setSimulator(simulator))
        
        simulation.configure()
        self.assertEquals(3, simulation.countSimulationEventQueues())
        
        connectEvent1 = self.SimulationEventForTest("CONNECT", str(randint(0, 1000)), 1)
        self.assertEquals(connectEvent1, simulation.registerSimulationEvent(connectEvent1))
        self.assertEquals(1, simulation.countSimulationEvents("CONNECT"))
        
        connectEvent2 = self.SimulationEventForTest("CONNECT", str(randint(0, 1000)), 2)
        self.assertEquals(connectEvent2, simulation.registerSimulationEvent(connectEvent2))
        self.assertEquals(2, simulation.countSimulationEvents("CONNECT"))
        
        disconnectEvent1 = self.SimulationEventForTest("DISCONNECT", str(randint(0, 1000)), 1)
        self.assertEquals(disconnectEvent1, simulation.registerSimulationEvent(disconnectEvent1))
        self.assertEquals(1, simulation.countSimulationEvents("DISCONNECT"))
        
        advertise1 = self.SimulationEventForTest("ADVERTISE", str(randint(0, 1000)), 1)
        self.assertEquals(advertise1, simulation.registerSimulationEvent(advertise1))
        self.assertEquals(1, simulation.countSimulationEvents("ADVERTISE"))
        
        advertise2 = self.SimulationEventForTest("ADVERTISE", str(randint(0, 1000)), 2)
        self.assertEquals(advertise2, simulation.registerSimulationEvent(advertise2))
        self.assertEquals(2, simulation.countSimulationEvents("ADVERTISE"))
        
        advertise3 = self.SimulationEventForTest("ADVERTISE", str(randint(0, 1000)), 3)
        self.assertEquals(advertise3, simulation.registerSimulationEvent(advertise3))
        self.assertEquals(3, simulation.countSimulationEvents("ADVERTISE"))
        
        self.assertEquals(advertise1, simulation.unregisterSimulationEvent("ADVERTISE"))
        self.assertEquals(2, simulation.countSimulationEvents("ADVERTISE"))
        
        self.assertEquals(disconnectEvent1, simulation.unregisterSimulationEvent("DISCONNECT"))
        self.assertEquals(0, simulation.countSimulationEvents("DISCONNECT"))
        
        self.assertEquals(connectEvent1, simulation.unregisterSimulationEvent("CONNECT"))
        self.assertEquals(1, simulation.countSimulationEvents("CONNECT"))
        self.assertEquals(connectEvent2, simulation.unregisterSimulationEvent("CONNECT"))
        self.assertEquals(0, simulation.countSimulationEvents("CONNECT"))
        
        self.assertEquals(advertise2, simulation.unregisterSimulationEvent("ADVERTISE"))
        self.assertEquals(1, simulation.countSimulationEvents("ADVERTISE"))
        self.assertEquals(advertise3, simulation.unregisterSimulationEvent("ADVERTISE"))
        self.assertEquals(0, simulation.countSimulationEvents("ADVERTISE"))
        
        self.assertRaises(TypeError, simulation.unregisterSimulationEvent, 1)
        self.assertRaises(TypeError, simulation.unregisterSimulationEvent, 0.8)
        self.assertRaises(TypeError, simulation.unregisterSimulationEvent, True)
        self.assertRaises(TypeError, simulation.unregisterSimulationEvent, False)
        
        self.assertRaises(InvalidValueError, simulation.unregisterSimulationEvent, None)
        self.assertRaises(InvalidValueError, simulation.unregisterSimulationEvent, "")
        
        self.assertRaises(UnregisterSimulationEventError, simulation.unregisterSimulationEvent, "BLAVLA")
    
    def testSetAndGetSimulationTime(self):
        simulation = self.SimulationForTest()
        self.assertEquals(1000, simulation.setSimulationTime(1000))
        self.assertEquals(1000, simulation.getSimulationTime())
        
        self.assertRaises(TypeError, simulation.setSimulationTime, "")
        self.assertRaises(TypeError, simulation.setSimulationTime, 0.1)
        
        self.assertRaises(InvalidValueError, simulation.setSimulationTime, 0)
        self.assertRaises(InvalidValueError, simulation.setSimulationTime, -1)
        
    def testSetAndGetCurrentSimulationTime(self):
        simulation = self.SimulationForTest()
        simulation.setSimulator(pymockobject.create(ISimulator))
        self.assertEquals(1500, simulation.setCurrentSimulationTime(1500))
        self.assertEquals(1500, simulation.getCurrentSimulationTime())
        
        self.assertRaises(TypeError, simulation.setCurrentSimulationTime, "")
        self.assertRaises(TypeError, simulation.setCurrentSimulationTime, 0.9)
        
        self.assertRaises(InvalidValueError, simulation.setCurrentSimulationTime, -1)
        self.assertRaises(InvalidValueError, simulation.setCurrentSimulationTime, 0)
    
    def testAddSimulationEventSimulator(self):
        simulation = self.SimulationForTest()
        
        generator1 = self.SimulationEventGeneratorForTest(1000)
        self.assertEquals(generator1, simulation.addSimulationEventGenerator(generator1))
        self.assertEquals(1, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        generator2 = self.SimulationEventGeneratorForTest(2000)
        self.assertEquals(generator2, simulation.addSimulationEventGenerator(generator2))
        self.assertEquals(2, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        generator3 = self.SimulationEventGeneratorForTest(2000)
        self.assertEquals(generator3, simulation.addSimulationEventGenerator(generator3))
        self.assertEquals(3, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        self.assertFalse(simulation.addSimulationEventGenerator(generator1))
        self.assertFalse(simulation.addSimulationEventGenerator(generator2))
        self.assertFalse(simulation.addSimulationEventGenerator(generator3))
        
        self.assertRaises(TypeError, simulation.addSimulationEventGenerator, "")
        self.assertRaises(TypeError, simulation.addSimulationEventGenerator, 1)
        self.assertRaises(TypeError, simulation.addSimulationEventGenerator, 1.0)
        self.assertRaises(TypeError, simulation.addSimulationEventGenerator, True)
        self.assertRaises(TypeError, simulation.addSimulationEventGenerator, False)
        
        self.assertRaises(InvalidValueError, simulation.addSimulationEventGenerator, None)
        
    def testRemoveSimulationEventGenerator(self):
        simulation = self.SimulationForTest()
        
        generator1 = self.SimulationEventGeneratorForTest(1000)
        self.assertEquals(generator1, simulation.addSimulationEventGenerator(generator1))
        self.assertEquals(1, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        generator2 = self.SimulationEventGeneratorForTest(2000)
        self.assertEquals(generator2, simulation.addSimulationEventGenerator(generator2))
        self.assertEquals(2, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        generator3 = self.SimulationEventGeneratorForTest(2000)
        self.assertEquals(generator3, simulation.addSimulationEventGenerator(generator3))
        self.assertEquals(3, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        self.assertEquals(generator2, simulation.removeSimulationEventGenerator(generator2))
        self.assertEquals(2, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        self.assertEquals(generator1, simulation.removeSimulationEventGenerator(generator1))
        self.assertEquals(1, simulation.countSimulationEventGenerators())
        self.assertTrue(simulation.getSimulationEventGenerators())
        
        self.assertEquals(generator3, simulation.removeSimulationEventGenerator(generator3))
        self.assertEquals(0, simulation.countSimulationEventGenerators())
        self.assertFalse(simulation.getSimulationEventGenerators())
        
        self.assertFalse(simulation.removeSimulationEventGenerator(generator1))
        self.assertFalse(simulation.removeSimulationEventGenerator(generator2))
        self.assertFalse(simulation.removeSimulationEventGenerator(generator3))
        
        self.assertRaises(TypeError, simulation.removeSimulationEventGenerator, "")
        self.assertRaises(TypeError, simulation.removeSimulationEventGenerator, 1)
        self.assertRaises(TypeError, simulation.removeSimulationEventGenerator, 0.5)
        self.assertRaises(TypeError, simulation.removeSimulationEventGenerator, True)
        self.assertRaises(TypeError, simulation.removeSimulationEventGenerator, False)
        
        self.assertRaises(InvalidValueError, simulation.registerSimulationEvent, None)
    
    
    
    class SimulationEventForTest(AbstractSimulationEvent):
        
        def __init__(self, handle, peer, priority):
            AbstractSimulationEvent.initialize(self, handle, peer, priority)
    
    class SimulationForTest(AbstractSimulation):
        
        def __init__(self):
            AbstractSimulation.initialize(self)
            
    class SimulationEventGeneratorForTest(AbstractSimulationEventGenerator):
        
        def __init__(self, generatedEvents):
            self.__generatedEvents = generatedEvents
            
        @public
        def generateSimulationEvents(self):
            return self.__generatedEvents