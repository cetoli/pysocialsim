from pysocialsim.p2p.message.default_p2p_message import DefaultP2PMessage
from pysocialsim.base.interface import implements
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
import unittest

class DefaultP2PMessageTest(unittest.TestCase):
    
    def setUp(self):
        self.__message = DefaultP2PMessage(12, 1, 2, 3)
        
    def test_implements_interface(self):
        self.assertTrue(implements(self.__message, IP2PMessage))
        
    def test_register_traces(self):
        self.assertEquals(3, self.__message.registerTrace(3))
        self.assertEquals(1, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(3, self.__message.getLastTrace())
        
        self.assertEquals(6, self.__message.registerTrace(6))
        self.assertEquals(2, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(6, self.__message.getLastTrace())
        
        self.assertEquals(1, self.__message.registerTrace(1))
        self.assertEquals(3, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(1, self.__message.getLastTrace())
        
        self.assertRaises(TypeError, self.__message.registerTrace, None)
        self.assertRaises(TypeError, self.__message.registerTrace, True)
        self.assertRaises(TypeError, self.__message.registerTrace, False)
        self.assertRaises(TypeError, self.__message.registerTrace, 0.2)
        self.assertRaises(TypeError, self.__message.registerTrace, "23")
        
    def test_unregister_traces(self):
        self.assertEquals(3, self.__message.registerTrace(3))
        self.assertEquals(1, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(3, self.__message.getLastTrace())
        
        self.assertEquals(6, self.__message.registerTrace(6))
        self.assertEquals(2, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(6, self.__message.getLastTrace())
        
        self.assertEquals(1, self.__message.registerTrace(1))
        self.assertEquals(3, self.__message.countTraces())
        self.assertEquals(3, self.__message.getFirstTrace())
        self.assertEquals(1, self.__message.getLastTrace())
        
        self.assertEquals(1, self.__message.unregisterTrace())
        self.assertEquals(2, self.__message.countTraces())
        self.assertEquals(6, self.__message.getLastTrace())
        
        self.assertEquals(6, self.__message.unregisterTrace())
        self.assertEquals(1, self.__message.countTraces())
        self.assertEquals(3, self.__message.getLastTrace())
        
        self.assertEquals(3, self.__message.unregisterTrace())
        self.assertEquals(0, self.__message.countTraces())
        
        self.assertRaises(StandardError, self.__message.unregisterTrace)
        self.assertRaises(StandardError, self.__message.getFirstTrace)
        self.assertRaises(StandardError, self.__message.getLastTrace)
    
    def test_set_parameters(self):
        self.assertEquals(1, self.__message.setParameter("test", 1))
        self.assertEquals(1, self.__message.countParameters())
        self.assertEquals(1, self.__message.getParameter("test"))
        
        self.assertEquals(True, self.__message.setParameter("boolean", True))
        self.assertEquals(2, self.__message.countParameters())
        self.assertEquals(True, self.__message.getParameter("boolean"))
        
        self.assertEquals(False, self.__message.setParameter("false", False))
        self.assertEquals(3, self.__message.countParameters())
        self.assertEquals(False, self.__message.getParameter("false"))
        
        self.assertRaises(TypeError, self.__message.setParameter, None, 1)
        self.assertRaises(TypeError, self.__message.setParameter, 1, 1)
        self.assertRaises(TypeError, self.__message.setParameter, 0.2, 1)
        self.assertRaises(TypeError, self.__message.setParameter, True, 1)
        self.assertRaises(TypeError, self.__message.setParameter, False, 1)
        