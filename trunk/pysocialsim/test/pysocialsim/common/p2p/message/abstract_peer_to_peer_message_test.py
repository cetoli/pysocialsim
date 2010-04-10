"""
Defines the module with the unit test of AbstractPeerToPeerMessage class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.peer.peer_id_generator import PeerIdGenerator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
import pymockobject

import unittest

class AbstractPeerToPeerMessageTest(unittest.TestCase):
    
    def testTryCreateClassInstance(self):
        self.assertRaises(NotImplementedError, AbstractPeertoPeerMessage)
        
    def testInitializationImplementation(self):
        message = self.PeerToPeerMessageForTest()
        
        self.assertEquals("Test", message.getHandle())
        self.assertEquals(0, message.getHop())
        self.assertEquals("", message.getId())
        self.assertEquals(0, message.getTTL())
        self.assertEquals("", message.getSourceId())
        self.assertEquals("", message.getTargetId())
        self.assertEquals(0, message.getPriority())
        
        peer = pymockobject.create(IPeer)
        peer.getId.will(ReturnValue(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)))
        id = PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer)
        sourceId = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        targetId = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        
        message.init(id, sourceId, targetId, 3, 1000)
        
        self.assertEquals(id, message.getId())
        self.assertEquals(sourceId, message.getSourceId())
        self.assertEquals(targetId, message.getTargetId())
        self.assertEquals(3, message.getTTL())
        self.assertEquals(1000, message.getPriority())
        
    def testCloneMessage(self):
        message = self.PeerToPeerMessageForTest()
        
        self.assertEquals("Test", message.getHandle())
        self.assertEquals(0, message.getHop())
        self.assertEquals("", message.getId())
        self.assertEquals(0, message.getTTL())
        self.assertEquals("", message.getSourceId())
        self.assertEquals("", message.getTargetId())
        self.assertEquals(0, message.getPriority())
        
        peer = pymockobject.create(IPeer)
        peer.getId.will(ReturnValue(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)))
        id = PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer)
        sourceId = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        targetId = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        
        message.init(id, sourceId, targetId, 3, 1000)
        
        self.assertEquals(id, message.getId())
        self.assertEquals(sourceId, message.getSourceId())
        self.assertEquals(targetId, message.getTargetId())
        self.assertEquals(3, message.getTTL())
        self.assertEquals(1000, message.getPriority())
        
        msgClone = message.clone()
        
        self.assertNotEquals(msgClone, message)
        self.assertEquals(msgClone.getHandle(), message.getHandle())
        self.assertEquals(msgClone.getId(), message.getId())
        self.assertEquals(msgClone.getSourceId(), message.getSourceId())
        self.assertEquals(msgClone.getTargetId(), message.getTargetId())
        self.assertEquals(msgClone.getTTL(), message.getTTL())
        self.assertEquals(msgClone.getPriority(), message.getPriority())
        
    
    class PeerToPeerMessageForTest(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, "Test")