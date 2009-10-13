"""
Defines the module with the unit test of GnutellaSuperPeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.p2p.protocol.gnutella.gnutella_super_peer_protocol import GnutellaSuperPeerProtocol
from pysocialsim.common.p2p.topology.abstract_peer_to_peer_topology import AbstractPeerToPeerTopology
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
import pymockobject

import unittest

class GnutellaSuperPeerProtocolTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(GnutellaSuperPeerProtocol())
        protocolo = GnutellaSuperPeerProtocol()
        self.assertFalse(protocolo.getPeerToPeerTopology())
        
    def testJoinSuperPeerInGnutellaNetwork(self):
        protocol = GnutellaSuperPeerProtocol()
        topology = self.TopologyForTest()
        network = pymockobject.create(IPeerToPeerNetwork)
        
        
        self.assertEquals(topology, protocol.setPeerToPeerTopology(topology))
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        peer1 = pymockobject.create(IPeer)
        peer1.isJoined.will(ReturnValue(True))
        peer1.getId.will(ReturnValue("1"))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "1").will(ReturnValue(peer1))
        
        self.assertFalse(protocol.join(peer1))
        
        peer2 = pymockobject.create(IPeer)
        peer2.isJoined.will(ReturnValue(False))
        peer2.getId.will(ReturnValue("2"))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "2").will(ReturnValue(peer2))
        
        self.assertTrue(protocol.join(peer2))
        self.assertEquals(1, topology.countNodes())
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue("3"))
        peer3.isJoined.will(ReturnValue(False))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "3").will(ReturnValue(peer3))
        
        peer4 = pymockobject.create(IPeer)
        peer4.getId.will(ReturnValue("4"))
        self.assertTrue(topology.addNode("4"))
        peer4.getNode.will(ReturnValue(topology.getNode("4")))
        topology.getNode("4").setPeer(peer4)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "4").will(ReturnValue(peer4))
        
        peer5 = pymockobject.create(IPeer)
        peer5.getId.will(ReturnValue("5"))
        self.assertTrue(topology.addNode("5"))
        peer5.getNode.will(ReturnValue(topology.getNode("5")))
        topology.getNode("5").setPeer(peer5)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "5").will(ReturnValue(peer5))
        
        peer6 = pymockobject.create(IPeer)
        peer6.getId.will(ReturnValue("6"))
        self.assertTrue(topology.addNode("6"))
        topology.getNode("6").setPeer(peer6)
        peer6.getNode.will(ReturnValue(topology.getNode("6")))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "6").will(ReturnValue(peer6))
        
        self.assertEquals(4, topology.countNodes())
        
        connectedPeers = [peer4, peer5, peer6]
        network.getConnectedPeers.expects(IPeerToPeerNetwork.SUPER_PEER).will(ReturnValue(connectedPeers.__iter__()))
        network.getConnectionsBetweenSuperPeers.will(ReturnValue(10))
        
        self.assertTrue(protocol.join(peer3))
        self.assertEquals(3, topology.countEdges("3"))
        
        self.assertRaises(TypeError, protocol.join, 1)
        self.assertRaises(TypeError, protocol.join, "1")
        self.assertRaises(TypeError, protocol.join, 0.88)
        self.assertRaises(TypeError, protocol.join, True)
        self.assertRaises(TypeError, protocol.join, False)
        
        self.assertRaises(InvalidValueError, protocol.join, None)
        
    def testLeaveuperPeerInGnutellaNetwork(self):
        protocol = GnutellaSuperPeerProtocol()
        topology = self.TopologyForTest()
        network = pymockobject.create(IPeerToPeerNetwork)
        
        
        self.assertEquals(topology, protocol.setPeerToPeerTopology(topology))
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        peer1 = pymockobject.create(IPeer)
        peer1.isJoined.will(ReturnValue(True))
        peer1.getId.will(ReturnValue("1"))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "1").will(ReturnValue(peer1))
        
        self.assertFalse(protocol.join(peer1))
        
        peer2 = pymockobject.create(IPeer)
        peer2.isJoined.will(ReturnValue(False))
        peer2.getId.will(ReturnValue("2"))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "2").will(ReturnValue(peer2))
        
        self.assertTrue(protocol.join(peer2))
        self.assertEquals(1, topology.countNodes())
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue("3"))
        peer3.isJoined.will(ReturnValue(False))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "3").will(ReturnValue(peer3))
        
        peer4 = pymockobject.create(IPeer)
        peer4.getId.will(ReturnValue("4"))
        self.assertTrue(topology.addNode("4"))
        peer4.getNode.will(ReturnValue(topology.getNode("4")))
        topology.getNode("4").setPeer(peer4)
        
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "4").will(ReturnValue(peer4))
        
        peer5 = pymockobject.create(IPeer)
        peer5.getId.will(ReturnValue("5"))
        self.assertTrue(topology.addNode("5"))
        peer5.getNode.will(ReturnValue(topology.getNode("5")))
        topology.getNode("5").setPeer(peer5)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "5").will(ReturnValue(peer5))
        
        peer6 = pymockobject.create(IPeer)
        peer6.getId.will(ReturnValue("6"))
        self.assertTrue(topology.addNode("6"))
        peer6.getNode.will(ReturnValue(topology.getNode("6")))
        topology.getNode("6").setPeer(peer6)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "6").will(ReturnValue(peer6))
        
        self.assertEquals(4, topology.countNodes())
        
        connectedPeers = [peer4, peer5, peer6]
        network.getConnectedPeers.expects(IPeerToPeerNetwork.SUPER_PEER).will(ReturnValue(connectedPeers.__iter__()))
        network.getConnectionsBetweenSuperPeers.will(ReturnValue(10))
        
        self.assertTrue(protocol.join(peer3))
        self.assertEquals(3, topology.countEdges("3"))
        
        peer7 = pymockobject.create(IPeer)
        peer7.isJoined.will(ReturnValue(False))
        
        self.assertFalse(protocol.leave(peer7))
        self.assertFalse(protocol.leave(peer2))
        
        peer3.getNode.will(ReturnValue(topology.getNode("3")))
        peer3.isJoined.will(ReturnValue(True))
        self.assertTrue(protocol.leave(peer3))
        
        self.assertEquals(0, topology.countEdges("3"))
        
        self.assertRaises(TypeError, protocol.leave, 1)
        self.assertRaises(TypeError, protocol.leave, 0.8)
        self.assertRaises(TypeError, protocol.leave, "teste")
        self.assertRaises(TypeError, protocol.leave, True)
        self.assertRaises(TypeError, protocol.leave, False)
        
        self.assertRaises(InvalidValueError, protocol.leave, None)
        peer = pymockobject.create(IPeer)
        peer.getNode.will(ReturnValue(None))
        self.assertRaises(InvalidValueError, protocol.leave, peer)
        
    def testCreatePeerToPeerMessage(self):
        protocol = GnutellaSuperPeerProtocol()
        self.assertTrue(protocol.createPeerToPeerMessage(IPeerToPeerProtocol.PING))
        
        
    class TopologyForTest(AbstractPeerToPeerTopology):
        
        def __init__(self):
            AbstractPeerToPeerTopology.initialize(self)
            
