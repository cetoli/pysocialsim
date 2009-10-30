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
from pysocialsim.common.p2p.network.peer_to_peer_network import PeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.p2p.topology.peer_to_peer_topology import PeerToPeerTopology
from pysocialsim.common.p2p.peer.super_peer import SuperPeer
from pysocialsim.common.p2p.peer.route import Route
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
import time
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
        peer4.countNeighbors.will(ReturnValue(1))
        topology.getNode("4").setPeer(peer4)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "4").will(ReturnValue(peer4))
        
        peer5 = pymockobject.create(IPeer)
        peer5.getId.will(ReturnValue("5"))
        self.assertTrue(topology.addNode("5"))
        peer5.getNode.will(ReturnValue(topology.getNode("5")))
        peer5.countNeighbors.will(ReturnValue(1))
        topology.getNode("5").setPeer(peer5)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "5").will(ReturnValue(peer5))
        
        peer6 = pymockobject.create(IPeer)
        peer6.getId.will(ReturnValue("6"))
        self.assertTrue(topology.addNode("6"))
        topology.getNode("6").setPeer(peer6)
        peer6.getNode.will(ReturnValue(topology.getNode("6")))
        peer6.countNeighbors.will(ReturnValue(1))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "6").will(ReturnValue(peer6))
        
        self.assertEquals(4, topology.countNodes())
        
        connectedPeers = [peer4, peer5, peer6]
        network.getConnectedPeers.expects(IPeerToPeerNetwork.SUPER_PEER).will(ReturnValue(connectedPeers.__iter__()))
        network.getConnectionsBetweenSuperPeers.will(ReturnValue(10))
        
        self.assertTrue(protocol.join(peer3))
        self.assertTrue(topology.countEdges("3") > 0)
        
        self.assertRaises(TypeError, protocol.join, 1)
        self.assertRaises(TypeError, protocol.join, "1")
        self.assertRaises(TypeError, protocol.join, 0.88)
        self.assertRaises(TypeError, protocol.join, True)
        self.assertRaises(TypeError, protocol.join, False)
        
        self.assertRaises(InvalidValueError, protocol.join, None)
        
    def testSendPeerToPeerMessageWithThreeHops(self):
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        network.setConnectionsBetweenSuperPeers(6)
        protocol = GnutellaSuperPeerProtocol()
        
        self.assertEquals(6, protocol.setPingHops(6))
        self.assertEquals(6, protocol.setPongHops(6))
        self.assertEquals(6, protocol.setPushHops(6))
        
        topology = PeerToPeerTopology()
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        self.assertEquals(topology, protocol.setPeerToPeerTopology(topology))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol))
        
        self.assertTrue(topology.addNode("1"))
        superPeer1 = SuperPeer("1", network)
        superPeer1.setNode(topology.getNode("1"))
        
        self.assertTrue(topology.addNode("2"))
        superPeer2 = SuperPeer("2", network)
        superPeer2.setNode(topology.getNode("2"))
        
        self.assertTrue(topology.addNode("3"))
        superPeer3 = SuperPeer("3", network)
        superPeer3.setNode(topology.getNode("3"))
        
        self.assertTrue(topology.addEdge("1", "2"))
        self.assertTrue(topology.addEdge("2", "1"))
        
        self.assertTrue(topology.addEdge("2", "3"))
        self.assertTrue(topology.addEdge("3", "2"))
        
        self.assertTrue(superPeer1.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("1"))
        self.assertTrue(superPeer3.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("3"))
        
        route = Route("3", ["3", "2"], 2, 0)
        
        self.assertEquals("2", superPeer1.getNeighbor("2").getId())
        neighbor = superPeer1.getNeighbor("2")
        self.assertTrue(neighbor.registerRoute(route))
        self.assertEquals(1, neighbor.countRoutes("3"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, IPeerToPeerProtocol.PUSH)
        message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(superPeer1), superPeer1.getId(), superPeer3.getId(), protocol.getPushHops(), 1)
        
        routeMessage = superPeer1.send(message)
        self.assertEquals(IPeerToPeerProtocol.ROUTE, routeMessage.getHandle())
        dispatcher = superPeer2.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer2.joined()
        dispatcher.on()
        
        time.sleep(1)
        dispatcher.off()
        
        dispatcher = superPeer3.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer3.joined()
        dispatcher.on()
        time.sleep(1)
        dispatcher.off()
    
    def testSendPeerToPeerMessageWithFourHops(self):
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        network.setConnectionsBetweenSuperPeers(6)
        protocol = GnutellaSuperPeerProtocol()
        
        self.assertEquals(6, protocol.setPingHops(6))
        self.assertEquals(6, protocol.setPongHops(6))
        self.assertEquals(6, protocol.setPushHops(6))
        
        topology = PeerToPeerTopology()
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        self.assertEquals(topology, protocol.setPeerToPeerTopology(topology))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol))
        
        self.assertTrue(topology.addNode("1"))
        superPeer1 = SuperPeer("1", network)
        superPeer1.setNode(topology.getNode("1"))
        
        self.assertTrue(topology.addNode("2"))
        superPeer2 = SuperPeer("2", network)
        superPeer2.setNode(topology.getNode("2"))
        
        self.assertTrue(topology.addNode("3"))
        superPeer3 = SuperPeer("3", network)
        superPeer3.setNode(topology.getNode("3"))
        
        self.assertTrue(topology.addNode("4"))
        superPeer4 = SuperPeer("4", network)
        superPeer4.setNode(topology.getNode("4"))
        
        self.assertTrue(topology.addEdge("1", "2"))
        self.assertTrue(topology.addEdge("2", "1"))
        
        self.assertTrue(topology.addEdge("2", "3"))
        self.assertTrue(topology.addEdge("3", "2"))
        
        self.assertTrue(topology.addEdge("3", "4"))
        self.assertTrue(topology.addEdge("4", "3"))
        
        self.assertTrue(superPeer1.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("1"))
        self.assertTrue(superPeer3.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("3"))
        self.assertTrue(superPeer3.hasNeighbor("4"))
        self.assertTrue(superPeer4.hasNeighbor("3"))
        
        route = Route("4", ["4", "3", "2"], 3, 0)
        
        self.assertEquals("2", superPeer1.getNeighbor("2").getId())
        neighbor = superPeer1.getNeighbor("2")
        self.assertTrue(neighbor.registerRoute(route))
        self.assertEquals(1, neighbor.countRoutes("4"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, IPeerToPeerProtocol.PUSH)
        message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(superPeer1), superPeer1.getId(), superPeer4.getId(), protocol.getPushHops(), 1)
        
        routeMessage = superPeer1.send(message)
        self.assertEquals(IPeerToPeerProtocol.ROUTE, routeMessage.getHandle())
        dispatcher = superPeer2.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer2.joined()
        dispatcher.on()

        time.sleep(0.1)
        
        time.sleep(1)
        dispatcher.off()
        
        dispatcher = superPeer3.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer3.joined()
        dispatcher.on()
        
        self.assertTrue(topology.addNode("4"))
        superPeer4 = SuperPeer("4", network)
        superPeer4.setNode(topology.getNode("4"))
        
        self.assertTrue(topology.addEdge("3", "4"))
        self.assertTrue(topology.addEdge("4", "3"))
        
        route = Route("4", ["4", "3", "2"], 3, 0)
        
        self.assertEquals("2", superPeer1.getNeighbor("2").getId())
        neighbor = superPeer1.getNeighbor("2")
        self.assertTrue(neighbor.registerRoute(route))
        self.assertEquals(1, neighbor.countRoutes("4"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, IPeerToPeerProtocol.PUSH)
        message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(superPeer1), superPeer1.getId(), superPeer4.getId(), protocol.getPushHops(), 1)
        
        superPeer1.send(message)
        
        time.sleep(0.1)
        dispatcher = superPeer4.getPeerToPeerMessageDispatcher()
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer4.joined()
        dispatcher.on()
        
        time.sleep(1)
        dispatcher.off()
        
        dispatcher = superPeer4.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer4.joined()
        dispatcher.on()
        
        time.sleep(1)
        
        dispatcher.off()
        
    def testSendPeerToPeerMessageWithTwoRoutes(self):
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        network.setConnectionsBetweenSuperPeers(6)
        protocol = GnutellaSuperPeerProtocol()
        
        
        self.assertEquals(6, protocol.setPingHops(6))
        self.assertEquals(6, protocol.setPongHops(6))
        self.assertEquals(6, protocol.setPushHops(6))
        
        topology = PeerToPeerTopology()
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        self.assertEquals(topology, protocol.setPeerToPeerTopology(topology))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol))
        
        self.assertTrue(topology.addNode("1"))
        superPeer1 = SuperPeer("1", network)
        superPeer1.setNode(topology.getNode("1"))
        
        self.assertTrue(topology.addNode("2"))
        superPeer2 = SuperPeer("2", network)
        superPeer2.setNode(topology.getNode("2"))
        
        self.assertTrue(topology.addNode("3"))
        superPeer3 = SuperPeer("3", network)
        superPeer3.setNode(topology.getNode("3"))
        
        self.assertTrue(topology.addNode("4"))
        superPeer4 = SuperPeer("4", network)
        superPeer4.setNode(topology.getNode("4"))
        
        self.assertTrue(topology.addEdge("1", "2"))
        self.assertTrue(topology.addEdge("2", "1"))
        
        self.assertTrue(topology.addEdge("2", "3"))
        self.assertTrue(topology.addEdge("3", "2"))
        
        self.assertTrue(topology.addEdge("2", "4"))
        self.assertTrue(topology.addEdge("4", "2"))
        
        self.assertTrue(topology.addEdge("3", "4"))
        self.assertTrue(topology.addEdge("4", "3"))
        
        self.assertTrue(superPeer1.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("1"))
        self.assertTrue(superPeer3.hasNeighbor("2"))
        self.assertTrue(superPeer2.hasNeighbor("3"))
        self.assertTrue(superPeer3.hasNeighbor("4"))
        self.assertTrue(superPeer4.hasNeighbor("3"))
        
        route = Route("4", ["4", "3", "2"], 3, 0)
        
        self.assertEquals("2", superPeer1.getNeighbor("2").getId())
        neighbor = superPeer1.getNeighbor("2")
        self.assertTrue(neighbor.registerRoute(route))
        self.assertEquals(1, neighbor.countRoutes("4"))
        
        route = Route("4", ["4", "2"], 2, 0)
        
        self.assertEquals("2", superPeer1.getNeighbor("2").getId())
        neighbor = superPeer1.getNeighbor("2")
        self.assertTrue(neighbor.registerRoute(route))
        self.assertEquals(2, neighbor.countRoutes("4"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, IPeerToPeerProtocol.PUSH)
        message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(superPeer1), superPeer1.getId(), superPeer4.getId(), protocol.getPushHops(), 1)
        
        routeMessage = superPeer1.send(message)
        self.assertEquals(IPeerToPeerProtocol.ROUTE, routeMessage.getHandle())
        dispatcher = superPeer2.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer2.joined()
        dispatcher.on()
        
        time.sleep(1)
        
        dispatcher.off()
        
        dispatcher = superPeer4.getPeerToPeerMessageDispatcher()
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        dispatcher.registerPeerToPeerMessageHandler(handler)
        self.assertEquals(1, dispatcher.countPeerToPeerMessages(IPeerToPeerProtocol.ROUTE))
        superPeer4.joined()
        dispatcher.on()
        
        time.sleep(1)
        
        dispatcher.off()
        
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
        peer4.countNeighbors.will(ReturnValue(1))
        topology.getNode("4").setPeer(peer4)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "4").will(ReturnValue(peer4))
        
        peer5 = pymockobject.create(IPeer)
        peer5.getId.will(ReturnValue("5"))
        self.assertTrue(topology.addNode("5"))
        peer5.getNode.will(ReturnValue(topology.getNode("5")))
        peer5.countNeighbors.will(ReturnValue(1))
        topology.getNode("5").setPeer(peer5)
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "5").will(ReturnValue(peer5))
        
        peer6 = pymockobject.create(IPeer)
        peer6.getId.will(ReturnValue("6"))
        self.assertTrue(topology.addNode("6"))
        topology.getNode("6").setPeer(peer6)
        peer6.getNode.will(ReturnValue(topology.getNode("6")))
        peer6.countNeighbors.will(ReturnValue(1))
        network.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "6").will(ReturnValue(peer6))
        
        self.assertEquals(4, topology.countNodes())
        
        connectedPeers = [peer4, peer5, peer6]
        network.getConnectedPeers.expects(IPeerToPeerNetwork.SUPER_PEER).will(ReturnValue(connectedPeers.__iter__()))
        network.getConnectionsBetweenSuperPeers.will(ReturnValue(10))
        
        self.assertTrue(protocol.join(peer3))
        self.assertTrue(topology.countEdges("3") > 0)
        
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
            
    class PeerToPeerMessageForTest(AbstractPeertoPeerMessage):
        
        def __init__(self, type, handle):
            AbstractPeertoPeerMessage.initialize(self, type, handle)
            
