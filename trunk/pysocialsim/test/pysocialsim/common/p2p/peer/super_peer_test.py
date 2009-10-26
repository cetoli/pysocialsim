"""
Defines the module with the unit test SimplePeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.p2p.peer.super_peer import SuperPeer
from pysocialsim.common.p2p.peer.peer_id_generator import PeerIdGenerator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.network.peer_to_peer_network import PeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.p2p.protocol.gnutella.gnutella_super_peer_protocol import GnutellaSuperPeerProtocol
from pysocialsim.common.p2p.topology.peer_to_peer_topology import PeerToPeerTopology
import pymockobject
import unittest

class SuperPeerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        peerToPeerNetwork = PeerToPeerNetwork(pymockobject.create(ISimulation))
        peerToPeerTopology = PeerToPeerTopology()
        peerToPeerProtocol = GnutellaSuperPeerProtocol()
        peerToPeerProtocol.setPeerToPeerTopology(peerToPeerTopology)
        peerToPeerNetwork.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, peerToPeerProtocol)
        
        self.assertTrue(SuperPeer(id, peerToPeerNetwork))
        
        superPeer = SuperPeer(id, peerToPeerNetwork)
        
        self.assertEquals(id, superPeer.getId())
        self.assertEquals(peerToPeerNetwork, superPeer.getPeerToPeerNetwork())
        self.assertFalse(superPeer.isJoined())
        self.assertTrue(superPeer.isLeaved())
        self.assertEquals(IPeerToPeerNetwork.SUPER_PEER, superPeer.getType())
        
    def testJoinPeerInGnutellaPeerToPeerNetwork(self):
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        peerToPeerNetwork = PeerToPeerNetwork(pymockobject.create(ISimulation))
        peerToPeerNetwork.setConnectionsBetweenSuperPeers(1)
        peerToPeerTopology = PeerToPeerTopology()
        peerToPeerTopology.setPeerToPeerNetwork(peerToPeerNetwork)
        peerToPeerProtocol = GnutellaSuperPeerProtocol()
        peerToPeerProtocol.setPeerToPeerTopology(peerToPeerTopology)
        peerToPeerNetwork.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, peerToPeerProtocol)
        
        superPeer1 = SuperPeer(id, peerToPeerNetwork)
        
        self.assertTrue(superPeer1.join())
        self.assertTrue(superPeer1.isJoined())
        self.assertFalse(superPeer1.isLeaved())
        self.assertTrue(superPeer1.getNode())
        self.assertEquals(0, superPeer1.countNeighbors())
        
        node1 = superPeer1.getNode()
        self.assertEquals(node1.getId(), superPeer1.getId())
        self.assertTrue(peerToPeerTopology.hasNode(node1.getId()))
        self.assertEquals(1, peerToPeerTopology.countNodes())
        self.assertEquals(0, node1.countEdges())
        
        self.assertTrue(peerToPeerNetwork.hasPeer(superPeer1))
        self.assertEquals(1, peerToPeerNetwork.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertEquals(superPeer1, peerToPeerNetwork.getPeer(IPeerToPeerNetwork.SUPER_PEER, superPeer1.getId()))
        
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        superPeer2 = SuperPeer(id, peerToPeerNetwork)
        
        self.assertTrue(superPeer2.join())
        self.assertTrue(superPeer2.isJoined())
        self.assertFalse(superPeer1.isLeaved())
        self.assertTrue(superPeer1.getNode())
        self.assertEquals(1, superPeer1.countNeighbors())
        self.assertEquals(1, superPeer2.countNeighbors())
        
        node2 = superPeer2.getNode()
        self.assertEquals(node2.getId(), superPeer2.getId())
        self.assertTrue(peerToPeerTopology.hasNode(node2.getId()))
        self.assertEquals(2, peerToPeerTopology.countNodes())
        self.assertEquals(1, node2.countEdges())
        
        self.assertTrue(node1.hasEdge(node2.getId()))
        self.assertTrue(node2.hasEdge(node1.getId()))
        
        self.assertTrue(peerToPeerNetwork.hasPeer(superPeer2))
        self.assertEquals(2, peerToPeerNetwork.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertEquals(superPeer2, peerToPeerNetwork.getPeer(IPeerToPeerNetwork.SUPER_PEER, superPeer2.getId()))
        
        id = PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER)
        superPeer3 = SuperPeer(id, peerToPeerNetwork)
        
        self.assertTrue(superPeer3.join())