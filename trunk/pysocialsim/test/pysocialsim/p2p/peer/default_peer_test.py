from pysocialsim.p2p.peer.default_peer import DefaultPeer
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.p2p.protocol.i_p2p_protocol import IP2PProtocol
from random import randint
from pysocialsim.base.interface import implements
from pysocialsim.p2p.peer.i_peer import IPeer
from pymockobject.events import ReturnValue
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.p2p.peer.event.send_event import SendEvent
from sets import ImmutableSet
import pymockobject
import unittest

class DefaultPeerTest(unittest.TestCase):
    
    def setUp(self):
        self.__network = pymockobject.create(IP2PNetwork)
        self.__protocol = pymockobject.create(IP2PProtocol)
        self.__protocol.getMessageHandlers.will(ReturnValue(ImmutableSet()))
        self.__peer = DefaultPeer(randint(1, 100), self.__network, self.__protocol)

    def test_implements_interface(self):
        self.assertTrue(implements(self.__peer, IPeer))
        
    def test_connect_peer(self):
        self.__peer.connect()
        self.assertFalse(self.__peer.isConnected())
        self.assertTrue(self.__peer.connected())
        self.assertTrue(self.__peer.isConnected())
        
        self.assertRaises(StandardError, self.__peer.connect)
        
    def test_disconnect_peer(self):
        self.__peer.connect()
        self.assertFalse(self.__peer.isConnected())
        self.assertTrue(self.__peer.connected())
        self.assertTrue(self.__peer.isConnected())
        
        self.__peer.disconnect()
        self.assertTrue(self.__peer.isConnected())
        self.assertTrue(self.__peer.disconnected())
        self.assertFalse(self.__peer.isConnected())
        
    def test_send(self):
        message = pymockobject.create(IP2PMessage)
        
        simulation = pymockobject.create(ISimulation)
        simulation.getSimulationCurrentTime.will(ReturnValue(1))
        
        self.__network.getSimulation.will(ReturnValue(simulation))
        event = SendEvent(self.__peer, simulation.getSimulationCurrentTime(), message)
        
        simulation.registerEvent.expects(event)
        
        self.assertEquals(message, self.__peer.send(message))
        
        self.assertRaises(TypeError, self.__peer.send, None)
        self.assertRaises(TypeError, self.__peer.send, 1)
        self.assertRaises(TypeError, self.__peer.send, True)
        self.assertRaises(TypeError, self.__peer.send, False)
        self.assertRaises(TypeError, self.__peer.send, "message")
        self.assertRaises(TypeError, self.__peer.send, 0.3)
        