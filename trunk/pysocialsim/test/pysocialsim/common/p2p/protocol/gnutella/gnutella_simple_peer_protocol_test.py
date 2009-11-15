"""
Defines the module with unit test of GnutellaSimplePeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 02/11/2009
"""
from pysocialsim.common.p2p.protocol.gnutella.gnutella_simple_peer_protocol import GnutellaSimplePeerProtocol
from pysocialsim.common.p2p.protocol.gnutella.gnutella_super_peer_protocol import GnutellaSuperPeerProtocol
from pysocialsim.common.p2p.network.peer_to_peer_network import PeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.p2p.topology.peer_to_peer_topology import PeerToPeerTopology
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.super_peer import SuperPeer
from pysocialsim.common.p2p.peer.simple_peer import SimplePeer
from pysocialsim.common.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
import time
import pymockobject

import unittest

class GnutellaSimplePeerProtocolTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(GnutellaSimplePeerProtocol())
        
        protocol = GnutellaSimplePeerProtocol()
        
        self.assertFalse(protocol.getPeerToPeerTopology())
        
        self.assertEquals(0, protocol.getPingHops())
        self.assertEquals(0, protocol.getPongHops())
        self.assertEquals(0, protocol.getPullHops())
        self.assertEquals(0, protocol.getPushHops())
        
    def testJoinSimplePeerInGnutellaNetwork(self):
        simplePeerProtocol = GnutellaSimplePeerProtocol()
        superPeerProtocol = GnutellaSuperPeerProtocol()
        
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        topology = PeerToPeerTopology()
        
        
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, superPeerProtocol))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, simplePeerProtocol))
                        
        self.assertEquals(topology, simplePeerProtocol.setPeerToPeerTopology(topology))
        self.assertEquals(topology, superPeerProtocol.setPeerToPeerTopology(topology))
        
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        self.assertEquals(1, network.setConnectionsBetweenSuperPeers(1))
        self.assertEquals(2, network.setConnectionsBetweenSuperPeerAndSimplePeers(2))
        self.assertEquals(1, network.setConnectionsBetweenSimplePeerAndSuperPeers(1))
        
        self.assertEquals(6, superPeerProtocol.setPingHops(6))
        self.assertEquals(6, superPeerProtocol.setPongHops(6))
        
        self.assertEquals(6, simplePeerProtocol.setPingHops(6))
        self.assertEquals(6, simplePeerProtocol.setPongHops(6))
        
        superPeer = SuperPeer("1", network)
        
        time.sleep(0.5)
        
        self.assertTrue(superPeer.join())
        
        simplePeer1 = SimplePeer("a", network)
        
        time.sleep(0.5)
        self.assertTrue(simplePeer1.join())
        
        self.assertEquals(1, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("a"))
        
        simplePeer2 = SimplePeer("b", network)
        
        time.sleep(0.5)
        self.assertTrue(simplePeer2.join())
        
        time.sleep(0.5)
        
        self.assertEquals(2, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("b"))
        
        self.assertTrue(simplePeer1.getNeighbor("1"))
        self.assertTrue(simplePeer2.getNeighbor("1"))
        
        neighbor1 = simplePeer1.getNeighbor("1")
        self.assertEquals("1", neighbor1.getId())
        self.assertTrue(neighbor1.hasRoutes("b"))
        
        neighbor2 = simplePeer2.getNeighbor("1")
        self.assertEquals("1", neighbor2.getId())
        self.assertTrue(neighbor2.hasRoutes("a"))
        
        simplePeer1.leave()
        simplePeer2.leave()
        superPeer.leave()
        
    def testLeaveSimplePeerInGnutellaNetwork(self):
        simplePeerProtocol = GnutellaSimplePeerProtocol()
        superPeerProtocol = GnutellaSuperPeerProtocol()
        
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        topology = PeerToPeerTopology()
        
        
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, superPeerProtocol))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, simplePeerProtocol))
                        
        self.assertEquals(topology, simplePeerProtocol.setPeerToPeerTopology(topology))
        self.assertEquals(topology, superPeerProtocol.setPeerToPeerTopology(topology))
        
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        self.assertEquals(1, network.setConnectionsBetweenSuperPeers(1))
        self.assertEquals(2, network.setConnectionsBetweenSuperPeerAndSimplePeers(2))
        self.assertEquals(1, network.setConnectionsBetweenSimplePeerAndSuperPeers(1))
        
        self.assertEquals(6, superPeerProtocol.setPingHops(6))
        self.assertEquals(6, superPeerProtocol.setPongHops(6))
        
        self.assertEquals(6, simplePeerProtocol.setPingHops(6))
        self.assertEquals(6, simplePeerProtocol.setPongHops(6))
        
        superPeer = SuperPeer("1", network)
        
        time.sleep(1)
        
        self.assertTrue(superPeer.join())
        
        simplePeer1 = SimplePeer("a", network)
        
        time.sleep(1)
        self.assertTrue(simplePeer1.join())
        
        self.assertEquals(1, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("a"))
        
        simplePeer2 = SimplePeer("b", network)
        
        time.sleep(1)
        self.assertTrue(simplePeer2.join())
        
        time.sleep(1)
        
        self.assertEquals(2, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("b"))
        
        self.assertTrue(simplePeer1.getNeighbor("1"))
        self.assertTrue(simplePeer2.getNeighbor("1"))
        
        neighbor1 = simplePeer1.getNeighbor("1")
        self.assertEquals("1", neighbor1.getId())
        self.assertTrue(neighbor1.hasRoutes("b"))
        
        neighbor2 = simplePeer2.getNeighbor("1")
        self.assertEquals("1", neighbor2.getId())
        self.assertTrue(neighbor2.hasRoutes("a"))
        
        self.assertTrue(simplePeer1.leave())
        self.assertFalse(simplePeer1.getNode())
        self.assertEquals(0, simplePeer1.countNeighbors())
        self.assertTrue(simplePeer1.isLeaved())
        self.assertFalse(simplePeer1.isJoined())
        
        self.assertEquals(1, superPeer.countChildren())
        
        simplePeer2.leave()
        self.assertFalse(simplePeer2.getNode())
        self.assertEquals(0, simplePeer2.countNeighbors())
        self.assertTrue(simplePeer2.isLeaved())
        self.assertFalse(simplePeer2.isJoined())
        
        self.assertEquals(0, superPeer.countChildren())
        
        superPeer.leave()
        
        
    def testSendPeerToPeerMessageForPeerInSameSuperPeer(self):
        simplePeerProtocol = GnutellaSimplePeerProtocol()
        superPeerProtocol = GnutellaSuperPeerProtocol()
        
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        topology = PeerToPeerTopology()
        
        
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, superPeerProtocol))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, simplePeerProtocol))
                        
        self.assertEquals(topology, simplePeerProtocol.setPeerToPeerTopology(topology))
        self.assertEquals(topology, superPeerProtocol.setPeerToPeerTopology(topology))
        
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        self.assertEquals(1, network.setConnectionsBetweenSuperPeers(1))
        self.assertEquals(2, network.setConnectionsBetweenSuperPeerAndSimplePeers(2))
        self.assertEquals(1, network.setConnectionsBetweenSimplePeerAndSuperPeers(1))
        
        self.assertEquals(6, superPeerProtocol.setPingHops(6))
        self.assertEquals(6, superPeerProtocol.setPongHops(6))
        
        self.assertEquals(6, simplePeerProtocol.setPingHops(6))
        self.assertEquals(6, simplePeerProtocol.setPongHops(6))
        
        superPeer = SuperPeer("1", network)
        
        time.sleep(1)
        
        self.assertTrue(superPeer.join())
        
        simplePeer1 = SimplePeer("a", network)
        
        time.sleep(1)
        self.assertTrue(simplePeer1.join())
        
        self.assertEquals(1, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("a"))
        
        simplePeer2 = SimplePeer("b", network)
        
        time.sleep(1)
        self.assertTrue(simplePeer2.join())
        
        time.sleep(1)
        
        self.assertEquals(2, superPeer.countChildren())
        self.assertTrue(superPeer.getNeighbor("b"))
        
        self.assertTrue(simplePeer1.getNeighbor("1"))
        self.assertTrue(simplePeer2.getNeighbor("1"))
        
        neighbor1 = simplePeer1.getNeighbor("1")
        self.assertEquals("1", neighbor1.getId())
        self.assertTrue(neighbor1.hasRoutes("b"))
        
        neighbor2 = simplePeer2.getNeighbor("1")
        self.assertEquals("1", neighbor2.getId())
        self.assertTrue(neighbor2.hasRoutes("a"))
        
        handler = pymockobject.create(IPeerToPeerMessageHandler)
        handler.getHandle.will(ReturnValue("PUSH"))
        handler.clone.will(ReturnValue(handler))
        
        dispatcher = simplePeer1.getPeerToPeerMessageDispatcher()
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        
        dispatcher = simplePeer2.getPeerToPeerMessageDispatcher()
        self.assertTrue(dispatcher.registerPeerToPeerMessageHandler(handler))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer1.getId(), simplePeer2.getId(), 3, 111)
        
        
        self.assertEquals(message, simplePeer1.send(message))
        
        time.sleep(0.5)
        
        self.assertTrue(simplePeer1.leave())
        self.assertFalse(simplePeer1.getNode())
        self.assertEquals(0, simplePeer1.countNeighbors())
        self.assertTrue(simplePeer1.isLeaved())
        self.assertFalse(simplePeer1.isJoined())
        
        self.assertEquals(1, superPeer.countChildren())
        
        simplePeer2.leave()
        self.assertFalse(simplePeer2.getNode())
        self.assertEquals(0, simplePeer2.countNeighbors())
        self.assertTrue(simplePeer2.isLeaved())
        self.assertFalse(simplePeer2.isJoined())
        
        self.assertEquals(0, superPeer.countChildren())
        
        superPeer.leave()
    
    def testSendPeerToPeerMessageForPeerInDiferentSuperPeers(self):
        simplePeerProtocol = GnutellaSimplePeerProtocol()
        superPeerProtocol = GnutellaSuperPeerProtocol()
        
        network = PeerToPeerNetwork(pymockobject.create(ISimulation))
        topology = PeerToPeerTopology()
        
        
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, superPeerProtocol))
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, simplePeerProtocol))
                        
        self.assertEquals(topology, simplePeerProtocol.setPeerToPeerTopology(topology))
        self.assertEquals(topology, superPeerProtocol.setPeerToPeerTopology(topology))
        
        self.assertEquals(network, topology.setPeerToPeerNetwork(network))
        
        self.assertEquals(1, network.setConnectionsBetweenSuperPeers(1))
        self.assertEquals(2, network.setConnectionsBetweenSuperPeerAndSimplePeers(2))
        self.assertEquals(1, network.setConnectionsBetweenSimplePeerAndSuperPeers(1))
        
        self.assertEquals(6, superPeerProtocol.setPingHops(6))
        self.assertEquals(6, superPeerProtocol.setPongHops(6))
        
        self.assertEquals(6, simplePeerProtocol.setPingHops(6))
        self.assertEquals(6, simplePeerProtocol.setPongHops(6))
        
        superPeer1 = SuperPeer("1", network)
        
        self.assertTrue(superPeer1.join())
        time.sleep(1)
        self.assertTrue(superPeer1.isJoined())
        self.assertEquals(0, superPeer1.countChildren())
        self.assertEquals(0, superPeer1.countNeighbors())
        
        simplePeer1 = SimplePeer("a", network)
        
        self.assertTrue(simplePeer1.join())
        time.sleep(1)
        self.assertTrue(simplePeer1.joined())
        self.assertEquals(1, simplePeer1.countNeighbors())
        
        simplePeer2 = SimplePeer("b", network)
        
        self.assertTrue(simplePeer2.join())
        time.sleep(1)
        self.assertTrue(simplePeer2.joined())
        self.assertEquals(1, simplePeer2.countNeighbors())
        
        superPeer2 = SuperPeer("2", network)
        
        self.assertTrue(superPeer2.join())
        time.sleep(1)
        self.assertTrue(superPeer2.isJoined())
        self.assertEquals(0, superPeer2.countChildren())
        self.assertEquals(1, superPeer2.countNeighbors())
        self.assertTrue(superPeer2.getNeighbor("1"))
        
        simplePeer3 = SimplePeer("c", network)
        
        self.assertTrue(simplePeer3.join())
        time.sleep(1)
        self.assertTrue(simplePeer3.joined())
        self.assertEquals(1, simplePeer3.countNeighbors())
        
        simplePeer4 = SimplePeer("d", network)
        
        self.assertTrue(simplePeer4.join())
        time.sleep(1)
        self.assertTrue(simplePeer4.joined())
        self.assertEquals(1, simplePeer4.countNeighbors())
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer1.getId(), simplePeer4.getId(), 6, 111)
        
        self.assertTrue(simplePeer1.getNeighbor("1"))
        neighbor1 = simplePeer1.getNeighbor("1")
        self.assertTrue(neighbor1.hasRoutes("b"))
        self.assertTrue(neighbor1.hasRoutes("c"))
        self.assertTrue(neighbor1.hasRoutes("d"))
        
        simplePeer1.send(message)
        
        time.sleep(0.5)
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer1.getId(), simplePeer3.getId(), 6, 111)
        
        simplePeer1.send(message)
        
        time.sleep(0.5)
        
        self.assertTrue(simplePeer2.getNeighbor("1"))
        neighbor2 = simplePeer2.getNeighbor("1")
        self.assertTrue(neighbor2.hasRoutes("a"))
        self.assertTrue(neighbor2.hasRoutes("c"))
        self.assertTrue(neighbor2.hasRoutes("d"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer2.getId(), simplePeer4.getId(), 6, 111)
        
        simplePeer2.send(message)
        
        time.sleep(0.5)
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer2.getId(), simplePeer3.getId(), 6, 111)
        
        simplePeer2.send(message)
        
        time.sleep(0.5)
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer4.getId(), simplePeer1.getId(), 6, 111)
        
        self.assertTrue(simplePeer4.getNeighbor("2"))
        neighbor1 = simplePeer4.getNeighbor("2")
        self.assertTrue(neighbor1.hasRoutes("a"))
        self.assertTrue(neighbor1.hasRoutes("b"))
        self.assertTrue(neighbor1.hasRoutes("c"))
        
        simplePeer4.send(message)
        
        time.sleep(0.5)
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer4.getId(), simplePeer2.getId(), 6, 111)
        
        simplePeer4.send(message)
        
        time.sleep(0.5)
        
        self.assertTrue(simplePeer3.getNeighbor("2"))
        neighbor2 = simplePeer3.getNeighbor("2")
        self.assertTrue(neighbor2.hasRoutes("a"))
        self.assertTrue(neighbor2.hasRoutes("b"))
        self.assertTrue(neighbor2.hasRoutes("d"))
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer3.getId(), simplePeer1.getId(), 6, 111)
        
        simplePeer3.send(message)
        
        time.sleep(0.5)
        
        message = self.PeerToPeerMessageForTest(IPeerToPeerMessage.SERVICE, "PUSH")
        message.init("aaa", simplePeer3.getId(), simplePeer2.getId(), 6, 111)
        
        simplePeer3.send(message)
        
        time.sleep(0.5)
        
        superPeer1.leave()
        simplePeer1.leave()
        simplePeer2.leave()
        
        superPeer2.leave()
        simplePeer3.leave()
        simplePeer4.leave()
    
    class PeerToPeerMessageForTest(AbstractPeertoPeerMessage):
        
        def __init__(self, type, handle):
            AbstractPeertoPeerMessage.initialize(self, type, handle)