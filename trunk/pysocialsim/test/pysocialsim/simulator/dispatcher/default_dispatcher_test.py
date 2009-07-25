from pysocialsim.simulator.dispatcher.default_dispatcher import DefaultDispatcher
from pysocialsim.base.interface import implements
from pysocialsim.simulator.dispatcher.i_dispatcher import IDispatcher
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from pymockobject.events import ReturnValue
from pysocialsim.simulator.event.i_event import IEvent
import pymockobject
import unittest

class DefaultDispatcherTest(unittest.TestCase):
    
    def setUp(self):
        self.__dispatcher = DefaultDispatcher()
    
    def test_implements_interfaces(self):
        self.assertTrue(implements(self.__dispatcher, IDispatcher))
        
    def test_register_event_handler(self):
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(1, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(2, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, None)
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, 1)
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, 0.8)
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, False)
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, True)
        self.assertRaises(TypeError, self.__dispatcher.registerEventHandler, "handler")
        
        self.assertFalse(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertFalse(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertFalse(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertFalse(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
    def test_unregister_event_handler(self):
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("CONNECT"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(1, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("DISCONNECT"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(2, self.__dispatcher.countEventHandlers())
        
        handler = pymockobject.create(IEventHandler)
        handler.getHandle.will(ReturnValue("ADVERTISE"))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        self.assertTrue(self.__dispatcher.unregisterEventHandler("CONNECT"))
        self.assertEquals(2, self.__dispatcher.countEventHandlers())
        
        self.assertTrue(self.__dispatcher.unregisterEventHandler("DISCONNECT"))
        self.assertEquals(1, self.__dispatcher.countEventHandlers())
        
        self.assertTrue(self.__dispatcher.unregisterEventHandler("ADVERTISE"))
        self.assertEquals(0, self.__dispatcher.countEventHandlers())
        
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, None)
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, 1)
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, 0.8)
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, False)
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, True)
        self.assertRaises(TypeError, self.__dispatcher.unregisterEventHandler, handler)
        
        self.assertFalse(self.__dispatcher.unregisterEventHandler("CONNECT"))
        self.assertEquals(0, self.__dispatcher.countEventHandlers())
        
        self.assertFalse(self.__dispatcher.unregisterEventHandler("DISCONNECT"))
        self.assertEquals(0, self.__dispatcher.countEventHandlers())
        
        self.assertFalse(self.__dispatcher.unregisterEventHandler("ADVERTISE"))
        self.assertEquals(0, self.__dispatcher.countEventHandlers())
    
    def test_handle_event(self):
        handler1 = pymockobject.create(IEventHandler)
        handler1.getHandle.will(ReturnValue("CONNECT"))
        handler1.clone.will(ReturnValue(handler1))
        
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler1))
        self.assertEquals(1, self.__dispatcher.countEventHandlers())
        
        handler2 = pymockobject.create(IEventHandler)
        handler2.getHandle.will(ReturnValue("DISCONNECT"))
        handler2.clone.will(ReturnValue(handler2))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler2))
        self.assertEquals(2, self.__dispatcher.countEventHandlers())
        
        handler3 = pymockobject.create(IEventHandler)
        handler3.getHandle.will(ReturnValue("ADVERTISE"))
        handler3.clone.will(ReturnValue(handler3))
        
        self.assertTrue(self.__dispatcher.registerEventHandler(handler3))
        self.assertEquals(3, self.__dispatcher.countEventHandlers())
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("CONNECT"))
        event.isHandled.will(ReturnValue(True))
        handler1.handleEvent.expects(event).will(ReturnValue(True))
        
        self.assertTrue(self.__dispatcher.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("DISCONNECT"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertTrue(self.__dispatcher.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("ADVERTISE"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertTrue(self.__dispatcher.handleEvent(event))
        
        event = pymockobject.create(IEvent)
        event.getHandle.will(ReturnValue("FILE"))
        event.isHandled.will(ReturnValue(True))
        
        self.assertFalse(self.__dispatcher.handleEvent(event))
        
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, None)
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, 1)
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, False)
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, True)
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, 0.2)
        self.assertRaises(TypeError, self.__dispatcher.handleEvent, "event")
        
        