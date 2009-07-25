from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.base.interface import implements
from pysocialsim.simulator.i_simulator import ISimulator
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from pymockobject.events import ReturnValue
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.simulator.simulation.stochastic.i_stochastic_simulation import IStochasticSimulation
import pymockobject
import unittest

class DefaultSimulatorTest(unittest.TestCase):
    
    def setUp(self):
        self.__simulator = DefaultSimulator()
        
    def test_implements_interfaces(self):
        self.assertTrue(implements(self.__simulator, ISimulator))
        
    def test_register_event_handlers(self):
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(1, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(2, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, None)
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, 1)
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, 0.8)
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, False)
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, True)
        self.assertRaises(TypeError, self.__simulator.registerEventHandler, "handler")
        
        self.assertFalse(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertFalse(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertFalse(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertFalse(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
    def test_unregister_event_handlers(self):
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(1, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(2, self.__simulator.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        self.assertTrue(self.__simulator.unregisterEventHandler("CONNECT"))
        self.assertEquals(2, self.__simulator.countEventHandlers())
        
        self.assertTrue(self.__simulator.unregisterEventHandler("DISCONNECT"))
        self.assertEquals(1, self.__simulator.countEventHandlers())
        
        self.assertTrue(self.__simulator.unregisterEventHandler("ADVERTISE"))
        self.assertEquals(0, self.__simulator.countEventHandlers())
        
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, None)
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, 1)
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, 0.8)
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, False)
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, True)
        self.assertRaises(TypeError, self.__simulator.unregisterEventHandler, handler)
        
        self.assertFalse(self.__simulator.unregisterEventHandler("CONNECT"))
        self.assertEquals(0, self.__simulator.countEventHandlers())
        
        self.assertFalse(self.__simulator.unregisterEventHandler("DISCONNECT"))
        self.assertEquals(0, self.__simulator.countEventHandlers())
        
        self.assertFalse(self.__simulator.unregisterEventHandler("ADVERTISE"))
        self.assertEquals(0, self.__simulator.countEventHandlers())
    
    def test_handle_event(self):
        handler1 = pymockobject.create(IEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        handler1.clone.will(ReturnValue(handler1))
        
        
        self.assertTrue(self.__simulator.registerEventHandler(handler1))
        self.assertEquals(1, self.__simulator.countEventHandlers())
        
        handler2 = pymockobject.create(IEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        handler2.clone.will(ReturnValue(handler2))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler2))
        self.assertEquals(2, self.__simulator.countEventHandlers())
        
        handler3 = pymockobject.create(IEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        handler3.clone.will(ReturnValue(handler3))
        
        self.assertTrue(self.__simulator.registerEventHandler(handler3))
        self.assertEquals(3, self.__simulator.countEventHandlers())
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("CONNECT"))
        event.isHandled.will(ReturnValue(True))
        handler1.handleEvent.expects(event).will(ReturnValue(True))
        
        self.assertTrue(self.__simulator.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("DISCONNECT"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertTrue(self.__simulator.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("ADVERTISE"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertTrue(self.__simulator.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("FILE"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertFalse(self.__simulator.handleEvent(event))
        
        self.assertRaises(TypeError, self.__simulator.handleEvent, None)
        self.assertRaises(TypeError, self.__simulator.handleEvent, 1)
        self.assertRaises(TypeError, self.__simulator.handleEvent, False)
        self.assertRaises(TypeError, self.__simulator.handleEvent, True)
        self.assertRaises(TypeError, self.__simulator.handleEvent, 0.2)
        self.assertRaises(TypeError, self.__simulator.handleEvent, "event")
        
    def test_create_stochastic_simulation(self):
        network = pymockobject.create(IP2PNetwork)
        
        self.assertTrue(self.__simulator.createStochasticSimulation(network))
        self.assertTrue(implements(self.__simulator.createStochasticSimulation(network), ISimulation, IStochasticSimulation))   
    