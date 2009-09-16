"""
Defines the module with the unit test of EventDispatcher class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""

from pysocialsim.common.simulator.event.event_dispatcher import EventDispatcher
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.simulator.i_simulator import ISimulator
from pymockobject.events import ReturnValue
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

class EventDispatcherTest(unittest.TestCase):
    
    def testInstantiateEventDispatcherClass(self):
        simulator = pymockobject.create(ISimulator)
        simulator.getSimulation.will(ReturnValue(pymockobject.create(ISimulation)))
        self.assertTrue(EventDispatcher(simulator))
        
    def testHandleSimulationEvent(self):
        simulator = pymockobject.create(ISimulator)
        simulator.getSimulation.will(ReturnValue(pymockobject.create(ISimulation)))
        dispatcher = EventDispatcher(simulator)
                
        self.assertFalse(dispatcher.handleSimulationEvent(self.SimulationEventForTest()))
        self.assertFalse(dispatcher.handleSimulationEvent(self.SimulationEventForTest_2()))
        
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest()))
        self.assertEquals(1, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest_2()))
        self.assertEquals(2, dispatcher.countSimulationEventHandlers())
        
        self.assertTrue(dispatcher.handleSimulationEvent(self.SimulationEventForTest()))
        self.assertTrue(dispatcher.handleSimulationEvent(self.SimulationEventForTest_2()))
        
        event = self.SimulationEventForTest()
        self.assertEquals(event, dispatcher.handleSimulationEvent(event))
        
        self.assertRaises(TypeError, dispatcher.handleSimulationEvent, 2)
        self.assertRaises(TypeError, dispatcher.handleSimulationEvent, "")
        self.assertRaises(TypeError, dispatcher.handleSimulationEvent, True)
        self.assertRaises(TypeError, dispatcher.handleSimulationEvent, False)
        self.assertRaises(TypeError, dispatcher.handleSimulationEvent, 2.4)
        
        self.assertRaises(InvalidValueError, dispatcher.handleSimulationEvent, None)
        
        
    def testRegisterSimulationEventHandler(self):
        simulator = pymockobject.create(ISimulator)
        simulator.getSimulation.will(ReturnValue(pymockobject.create(ISimulation)))
        dispatcher = EventDispatcher(simulator)
        
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest()))
        self.assertEquals(1, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest_2()))
        self.assertEquals(2, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        
        self.assertFalse(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest()))
        self.assertEquals(2, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        self.assertFalse(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest_2()))
        self.assertEquals(2, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        
        self.assertRaises(TypeError, dispatcher.registerSimulationEventHandler, 1)
        self.assertRaises(TypeError, dispatcher.registerSimulationEventHandler, "event")
        self.assertRaises(TypeError, dispatcher.registerSimulationEventHandler, True)
        self.assertRaises(TypeError, dispatcher.registerSimulationEventHandler, False)
        self.assertRaises(TypeError, dispatcher.registerSimulationEventHandler, 1.3)
        
        self.assertRaises(InvalidValueError, dispatcher.registerSimulationEventHandler, None)
        
    def testUnregisterSimulationEventHandler(self):
        simulator = pymockobject.create(ISimulator)
        simulator.getSimulation.will(ReturnValue(pymockobject.create(ISimulation)))
        dispatcher = EventDispatcher(simulator)
        
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest()))
        self.assertEquals(1, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        self.assertTrue(dispatcher.registerSimulationEventHandler(self.SimulationEventHandlerForTest_2()))
        self.assertEquals(2, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        
        self.assertTrue(dispatcher.unregisterSimulationEventHandler("EVENT_FOR_TEST"))
        self.assertEquals(1, dispatcher.countSimulationEventHandlers())
        self.assertTrue(dispatcher.getSimulationEventHandlers())
        self.assertTrue(dispatcher.unregisterSimulationEventHandler("EVENT_FOR_TEST_2"))
        self.assertEquals(0, dispatcher.countSimulationEventHandlers())
        self.assertFalse(dispatcher.getSimulationEventHandlers())
        
        self.assertFalse(dispatcher.unregisterSimulationEventHandler("EVENT_FOR_TEST"))
        self.assertEquals(0, dispatcher.countSimulationEventHandlers())
        self.assertFalse(dispatcher.getSimulationEventHandlers())
        self.assertFalse(dispatcher.unregisterSimulationEventHandler("EVENT_FOR_TEST_2"))
        self.assertEquals(0, dispatcher.countSimulationEventHandlers())
        self.assertFalse(dispatcher.getSimulationEventHandlers())
        
        self.assertRaises(TypeError, dispatcher.unregisterSimulationEventHandler, 0)
        self.assertRaises(TypeError, dispatcher.unregisterSimulationEventHandler, 0.8)
        self.assertRaises(TypeError, dispatcher.unregisterSimulationEventHandler, True)
        self.assertRaises(TypeError, dispatcher.unregisterSimulationEventHandler, False)
        
        self.assertRaises(InvalidValueError, dispatcher.unregisterSimulationEventHandler, None)
        self.assertRaises(InvalidValueError, dispatcher.unregisterSimulationEventHandler, "")
        
        
    class SimulationEventHandlerForTest(AbstractSimulationEventHandler):
        
        def __init__(self):
            AbstractSimulationEventHandler.initialize(self, "EVENT_FOR_TEST")

        def execute(self):
            pass
        
    class SimulationEventForTest(AbstractSimulationEvent):
        
        def __init__(self):
            AbstractSimulationEvent.initialize(self, "EVENT_FOR_TEST", None, None)
            
    class SimulationEventHandlerForTest_2(AbstractSimulationEventHandler):
        
        def __init__(self):
            AbstractSimulationEventHandler.initialize(self, "EVENT_FOR_TEST_2")

        def execute(self):
            pass
        
    class SimulationEventForTest_2(AbstractSimulationEvent):
        
        def __init__(self):
            AbstractSimulationEvent.initialize(self, "EVENT_FOR_TEST_2", None, None)