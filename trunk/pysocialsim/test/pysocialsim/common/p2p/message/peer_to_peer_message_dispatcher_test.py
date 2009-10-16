"""
Defines the module with the unit test of PeerToPeerMessageDispatcher class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""
from pysocialsim.common.p2p.message.peer_to_peer_message_dispatcher import PeerToPeerMessageDispatcher
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
import pymockobject

import unittest

class PeerToPeerMessageHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(PeerToPeerMessageDispatcher(pymockobject.create(IPeer)))
        
        dispatcher = PeerToPeerMessageDispatcher(pymockobject.create(IPeer))
        self.assertEquals(0, dispatcher.countPeerToPeerMessageHandler())
        
    def testRegisterPeerToPeerMessageHandler(self):
        dispatcher = PeerToPeerMessageDispatcher(pymockobject.create(IPeer))
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST1"))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(1, dispatcher.countPeerToPeerMessageHandler())
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST2"))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertFalse(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertRaises(InvalidValueError, dispatcher.registerPeerToPeerMessageHandler, None)
        
        self.assertRaises(TypeError, dispatcher.registerPeerToPeerMessageHandler, "test")
        self.assertRaises(TypeError, dispatcher.registerPeerToPeerMessageHandler, 1)
        self.assertRaises(TypeError, dispatcher.registerPeerToPeerMessageHandler, 0.56)
        self.assertRaises(TypeError, dispatcher.registerPeerToPeerMessageHandler, True)
        self.assertRaises(TypeError, dispatcher.registerPeerToPeerMessageHandler, False)
        
    def testUnregisterPeerToPeerMessageHandler(self):
        dispatcher = PeerToPeerMessageDispatcher(pymockobject.create(IPeer))
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST1"))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(1, dispatcher.countPeerToPeerMessageHandler())
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST2"))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertFalse(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertTrue(dispatcher.unregisterPeerToPeerMessageHandler("TEST1"))
        self.assertEquals(1, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertTrue(dispatcher.unregisterPeerToPeerMessageHandler("TEST2"))
        self.assertEquals(0, dispatcher.countPeerToPeerMessageHandler())
        
    def testHandleMessage(self):
        dispatcher = PeerToPeerMessageDispatcher(pymockobject.create(IPeer))
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST1"))
        handler.clone.will(ReturnValue(handler))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(1, dispatcher.countPeerToPeerMessageHandler())
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("TEST2"))
        handler.clone.will(ReturnValue(handler))
        
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        self.assertFalse(dispatcher.registerPeerToPeerMessageHandler(handler))
        self.assertEquals(2, dispatcher.countPeerToPeerMessageHandler())
        
        message = pymockobject.create(IPeerToPeerMessage)
        message.getHandle.will(ReturnValue("TEST1"))
        
        self.assertEquals(message, dispatcher.handlePeerToPeerMessage(message))
        
        message = pymockobject.create(IPeerToPeerMessage)
        message.getHandle.will(ReturnValue("TEST2"))
        
        self.assertEquals(message, dispatcher.handlePeerToPeerMessage(message))
        
        
        