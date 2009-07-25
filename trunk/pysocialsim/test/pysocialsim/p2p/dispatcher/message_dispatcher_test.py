from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.dispatcher.message_dispatcher import MessageDispatcher
from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler
from pymockobject.events import ReturnValue
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
import pymockobject
import unittest

class MessageDispatcherTest(unittest.TestCase):
    
    def setUp(self):
        self.__peer = pymockobject.create(IPeer)
        self.__dispatcher = MessageDispatcher(self.__peer)
    
    def test_register_message_handlers(self):
        handler1 = pymockobject.create(IMessageHandler)
        handler1.getMessageName.will(ReturnValue("CONNECT_PEER"))
        self.assertEquals(handler1, self.__dispatcher.registerMessageHandler(handler1))
        self.assertEquals(1, self.__dispatcher.countMessageHandlers())
        
        handler2 = pymockobject.create(IMessageHandler)
        handler2.getMessageName.will(ReturnValue("DISCONNECT_PEER"))
        self.assertEquals(handler2, self.__dispatcher.registerMessageHandler(handler2))
        self.assertEquals(2, self.__dispatcher.countMessageHandlers())
        
        handler3 = pymockobject.create(IMessageHandler)
        handler3.getMessageName.will(ReturnValue("ADVERTISE"))
        self.assertEquals(handler3, self.__dispatcher.registerMessageHandler(handler3))
        self.assertEquals(3, self.__dispatcher.countMessageHandlers())
        
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, None)
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, True)
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, False)
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, 1)
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, 1.0)
        self.assertRaises(TypeError, self.__dispatcher.registerMessageHandler, "handler")
        
        self.assertRaises(StandardError, self.__dispatcher.registerMessageHandler, handler1)
        self.assertRaises(StandardError, self.__dispatcher.registerMessageHandler, handler2)
        self.assertRaises(StandardError, self.__dispatcher.registerMessageHandler, handler3)
    
    def test_unregister_message_handlers(self):
        handler1 = pymockobject.create(IMessageHandler)
        handler1.getMessageName.will(ReturnValue("CONNECT_PEER"))
        self.assertEquals(handler1, self.__dispatcher.registerMessageHandler(handler1))
        self.assertEquals(1, self.__dispatcher.countMessageHandlers())
        
        handler2 = pymockobject.create(IMessageHandler)
        handler2.getMessageName.will(ReturnValue("DISCONNECT_PEER"))
        self.assertEquals(handler2, self.__dispatcher.registerMessageHandler(handler2))
        self.assertEquals(2, self.__dispatcher.countMessageHandlers())
        
        handler3 = pymockobject.create(IMessageHandler)
        handler3.getMessageName.will(ReturnValue("ADVERTISE"))
        self.assertEquals(handler3, self.__dispatcher.registerMessageHandler(handler3))
        self.assertEquals(3, self.__dispatcher.countMessageHandlers())
        
        self.assertEquals(handler1, self.__dispatcher.unregisterMessageHandler("CONNECT_PEER"))
        self.assertEquals(2, self.__dispatcher.countMessageHandlers())
        
        self.assertEquals(handler2, self.__dispatcher.unregisterMessageHandler("DISCONNECT_PEER"))
        self.assertEquals(1, self.__dispatcher.countMessageHandlers())
        
        self.assertEquals(handler3, self.__dispatcher.unregisterMessageHandler("ADVERTISE"))
        self.assertEquals(0, self.__dispatcher.countMessageHandlers())
    
    def test_handle_p2p_messages(self):
        handler1 = pymockobject.create(IMessageHandler)
        handler1.getMessageName.will(ReturnValue("CONNECT_PEER"))
        self.assertEquals(handler1, self.__dispatcher.registerMessageHandler(handler1))
        self.assertEquals(1, self.__dispatcher.countMessageHandlers())
        
        handler2 = pymockobject.create(IMessageHandler)
        handler2.getMessageName.will(ReturnValue("DISCONNECT_PEER"))
        self.assertEquals(handler2, self.__dispatcher.registerMessageHandler(handler2))
        self.assertEquals(2, self.__dispatcher.countMessageHandlers())
        
        handler3 = pymockobject.create(IMessageHandler)
        handler3.getMessageName.will(ReturnValue("ADVERTISE"))
        self.assertEquals(handler3, self.__dispatcher.registerMessageHandler(handler3))
        self.assertEquals(3, self.__dispatcher.countMessageHandlers())
        
        message1 = pymockobject.create(IP2PMessage)
        message1.getName.will(ReturnValue("CONNECT_PEER"))
        
        self.assertEquals(message1, self.__dispatcher.handleP2PMessage(message1))
        
        message2 = pymockobject.create(IP2PMessage)
        message2.getName.will(ReturnValue("DISCONNECT_PEER"))
        
        self.assertEquals(message2, self.__dispatcher.handleP2PMessage(message2))
        
        message3 = pymockobject.create(IP2PMessage)
        message3.getName.will(ReturnValue("ADVERTISE"))
        
        self.assertEquals(message3, self.__dispatcher.handleP2PMessage(message3))