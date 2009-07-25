from pysocialsim.p2p.peer.event.receive_event import ReceiveEvent
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
from pysocialsim.base.interface import implements
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.p2p.peer.event.i_peer_event import IPeerEvent
import pymockobject
import unittest

class ReceiveEventTest(unittest.TestCase):
    
    def setUp(self):
        self.__peer = pymockobject.create(IPeer)
        self.__message = pymockobject.create(IP2PMessage)
        self.__event = ReceiveEvent(self.__peer, 2, self.__message)
        
    def test_implements_interface(self):
        self.assertTrue(implements(self.__event, IEvent, IPeerEvent))
    
    def test_get_handle(self):
        self.assertEquals("RECEIVE_MESSAGE", self.__event.getHandle())
        
    def test_get_peer(self):
        self.assertEquals(self.__peer, self.__event.getPeer())
    
    def test_get_p2p_message(self):
        self.assertEquals(self.__message, self.__event.getP2PMessage())
        
    def test_get_priority(self):
        self.assertEquals(2, self.__event.getPriority())