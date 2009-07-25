from pysocialsim.p2p.peer.event.send_event import SendEvent
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.p2p.peer.event.i_peer_event import IPeerEvent
from pysocialsim.base.interface import implements
import pymockobject
import unittest

class SendEventTest(unittest.TestCase):
    
    def setUp(self):
        self.__peer = pymockobject.create(IPeer)
        self.__message = pymockobject.create(IP2PMessage)
        self.__event = SendEvent(self.__peer, 1, self.__message)
        
    def test_implements_interface(self):
        self.assertTrue(implements(self.__event, IEvent, IPeerEvent))
    
    def test_get_handle(self):
        self.assertEquals("SEND_MESSAGE", self.__event.getHandle())
        
    def test_get_peer(self):
        self.assertEquals(self.__peer, self.__event.getPeer())
    
    def test_get_p2p_message(self):
        self.assertEquals(self.__message, self.__event.getP2PMessage())
        
    def test_get_priority(self):
        self.assertEquals(1, self.__event.getPriority())