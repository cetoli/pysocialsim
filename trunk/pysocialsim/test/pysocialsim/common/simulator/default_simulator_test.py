"""
Defines the module with the unit test fo DefaultSimulator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/08/2009
"""
from pysocialsim.common.simulator.default_simulator import DefaultSimulator
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pymockobject.events import ReturnValue
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.error.invalid_value_error import InvalidValueError
import time
import pymockobject

import unittest

class DefaultSimulatorTest(unittest.TestCase):
    
    def testCreateInstance(self):
        self.assertTrue(DefaultSimulator())
        self.assertFalse(DefaultSimulator().getSimulation())
        self.assertFalse(DefaultSimulator().getSimulationEventHandlers())
        self.assertTrue(DefaultSimulator().getScheduler())
        
    def testHandleSimulationEvent(self):
        simulator = DefaultSimulator()
        
        simulationEvent1 = pymockobject.create(ISimulationEvent)
        simulationEvent1.getHandle.will(ReturnValue("CONNECT"))
        self.assertFalse(simulator.handleSimulationEvent(simulationEvent1))
        
        handler = pymockobject.create(ISimulationEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        handlerClone = pymockobject.create(ISimulationEventHandler)
        handler.clone.will(ReturnValue(handlerClone))
        handlerClone.handleSimulationEvent.expects(simulationEvent1).will(ReturnValue(simulationEvent1))
        handlerClone.init.expects(pymockobject.create(ISimulation))
        
        self.assertTrue(simulator.registerSimulationEventHandler(handler))
        self.assertEquals(simulationEvent1, simulator.handleSimulationEvent(simulationEvent1))
        
        self.assertRaises(TypeError, simulator.handleSimulationEvent, 1)
        self.assertRaises(TypeError, simulator.handleSimulationEvent, 1.3)
        self.assertRaises(TypeError, simulator.handleSimulationEvent, "")
        self.assertRaises(TypeError, simulator.handleSimulationEvent, True)
        self.assertRaises(TypeError, simulator.handleSimulationEvent, False)
        
        self.assertRaises(InvalidValueError, simulator.handleSimulationEvent, None)
    
    def testRegisterSimulationEventHandler(self):
        simulator = DefaultSimulator()
        
        handler1 = pymockobject.create(ISimulationEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler1))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler2 = pymockobject.create(ISimulationEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler2))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler3 = pymockobject.create(ISimulationEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler3))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        self.assertFalse(simulator.registerSimulationEventHandler(handler1))
        self.assertFalse(simulator.registerSimulationEventHandler(handler2))
        self.assertFalse(simulator.registerSimulationEventHandler(handler3))
        
        self.assertRaises(TypeError, simulator.registerSimulationEventHandler, "")
        self.assertRaises(TypeError, simulator.registerSimulationEventHandler, 1)
        self.assertRaises(TypeError, simulator.registerSimulationEventHandler, 0.55)
        self.assertRaises(TypeError, simulator.registerSimulationEventHandler, True)
        self.assertRaises(TypeError, simulator.registerSimulationEventHandler, False)
        
        self.assertRaises(InvalidValueError, simulator.registerSimulationEventHandler, None)
    
    def testUnregisterSimulationEventHandler(self):
        simulator = DefaultSimulator()
        
        handler1 = pymockobject.create(ISimulationEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler1))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler2 = pymockobject.create(ISimulationEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler2))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler3 = pymockobject.create(ISimulationEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler3))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        self.assertTrue(simulator.unregisterSimulationEventHandler("CONNECT"))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        self.assertTrue(simulator.unregisterSimulationEventHandler("DISCONNECT"))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        self.assertTrue(simulator.unregisterSimulationEventHandler("ADVERTISE"))
        self.assertEquals(0, simulator.countSimulationEventHandlers())
        self.assertFalse(simulator.getSimulationEventHandlers())
        
        self.assertFalse(simulator.unregisterSimulationEventHandler("CONNECT"))
        self.assertFalse(simulator.unregisterSimulationEventHandler("DISCONNECT"))
        self.assertFalse(simulator.unregisterSimulationEventHandler("ADVERTISE"))
    
    def testStartAndStopSimulation(self):
        simulator = DefaultSimulator()
        
        simulationEvent1 = pymockobject.create(ISimulationEvent)
        simulationEvent1.getHandle.will(ReturnValue("EXIT"))
        self.assertFalse(simulator.handleSimulationEvent(simulationEvent1))

        simulation = pymockobject.create(ISimulation)
        simulation.unregisterSimulationEvent.expects("EXIT").will(ReturnValue(simulationEvent1))
        simulation.getCurrentSimulationTime.will(ReturnValue(12))
        simulation.getSimulationTime.will(ReturnValue(2000))
        simulation.countSimulationEvents.will(ReturnValue(3))
        simulation.getSimulationEvent.will(ReturnValue(pymockobject.create(ISimulationEvent)))
        self.assertEquals(simulation, simulator.setSimulation(simulation))
    
        handler1 = pymockobject.create(ISimulationEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler1))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler2 = pymockobject.create(ISimulationEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler2))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler3 = pymockobject.create(ISimulationEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler3))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        simulator.start()
        time.sleep(1)
        simulation.countSimulationEvents.will(ReturnValue(0))
        simulator.stop()
    
    def testNotifyEventHandlingThreads(self):
        simulator = DefaultSimulator()

        handler1 = pymockobject.create(ISimulationEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler1))
        self.assertEquals(1, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler2 = pymockobject.create(ISimulationEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler2))
        self.assertEquals(2, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        handler3 = pymockobject.create(ISimulationEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        self.assertTrue(simulator.registerSimulationEventHandler(handler3))
        self.assertEquals(3, simulator.countSimulationEventHandlers())
        self.assertTrue(simulator.getSimulationEventHandlers())
        
        simulation = pymockobject.create(ISimulation)
        simulation.getCurrentSimulationTime.will(ReturnValue(12))
        simulation.getSimulationTime.will(ReturnValue(2000))
        simulation.countSimulationEvents.will(ReturnValue(3))
        simulation.getSimulationEvent.will(ReturnValue(pymockobject.create(ISimulationEvent)))
        self.assertEquals(simulation, simulator.setSimulation(simulation))
        
        simulator.start()
        simulator.notifyEventHandlingThreads()
        time.sleep(1)
        simulation.countSimulationEvents.will(ReturnValue(0))
        simulator.stop()