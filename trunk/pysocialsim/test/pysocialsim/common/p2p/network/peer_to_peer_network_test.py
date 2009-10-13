"""
Defines the module with the unit test of PeerToPeerNetwork class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/10/2009
"""
from pysocialsim.common.p2p.network.peer_to_peer_network import PeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.p2p.peer.super_peer import SuperPeer
from pysocialsim.common.p2p.peer.peer_id_generator import PeerIdGenerator
from pysocialsim.common.p2p.peer.simple_peer import SimplePeer
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class PeerToPeerNetworkTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(PeerToPeerNetwork(pymockobject.create(ISimulation)))
        simulation = pymockobject.create(ISimulation)
        
        network = PeerToPeerNetwork(simulation)
        
        self.assertEquals(simulation, network.getSimulation())
        self.assertEquals(0, network.getConnectionsBetweenSuperPeers())
        
        self.assertTrue(network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(network.getConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertTrue(network.getDisconnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(network.getDisconnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertEquals(0, network.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertEquals(0, network.countPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertTrue(network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
    
    def testSetAndGetConnectionsBetweenSuperPeers(self):
        simulation = pymockobject.create(ISimulation)
        network = PeerToPeerNetwork(simulation)
        
        self.assertEquals(10, network.setConnectionsBetweenSuperPeers(10))
        self.assertEquals(10, network.getConnectionsBetweenSuperPeers())
        
        self.assertRaises(TypeError, network.setConnectionsBetweenSuperPeers, "")
        self.assertRaises(TypeError, network.setConnectionsBetweenSuperPeers, 0.99)
        
        self.assertRaises(InvalidValueError, network.setConnectionsBetweenSuperPeers, None)
        self.assertRaises(InvalidValueError, network.setConnectionsBetweenSuperPeers, 0)
        self.assertRaises(InvalidValueError, network.setConnectionsBetweenSuperPeers, -1)
        
    def testSetAndGetSimulation(self):
        simulation = pymockobject.create(ISimulation)
        network = PeerToPeerNetwork(simulation)
        
        simulation1 = pymockobject.create(ISimulation)
        self.assertEquals(simulation1, network.setSimulation(simulation1))
        self.assertEquals(simulation1, network.getSimulation())
        
        self.assertRaises(TypeError, network.setSimulation, "")
        self.assertRaises(TypeError, network.setSimulation, 1)
        self.assertRaises(TypeError, network.setSimulation, 0.8)
        self.assertRaises(TypeError, network.setSimulation, True)
        self.assertRaises(TypeError, network.setSimulation, False)
        
        self.assertRaises(InvalidValueError, network.setSimulation, None)
    
    def testAddPeerInPeerToPeerNetwork(self):
        simulation = pymockobject.create(ISimulation)
        network = PeerToPeerNetwork(simulation)
        
        superPeer1 = SuperPeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER), pymockobject.create(IPeerToPeerNetwork))
        superPeer1.joined()
        
        self.assertTrue(network.addPeer(IPeerToPeerNetwork.SUPER_PEER, superPeer1))
        self.assertEquals(1, network.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(superPeer1 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(not superPeer1 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(superPeer1 in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(not superPeer1 in network.getDisconnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        
        superPeer2 = SuperPeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER), pymockobject.create(IPeerToPeerNetwork))
        superPeer2.leaved()
        
        self.assertTrue(network.addPeer(IPeerToPeerNetwork.SUPER_PEER, superPeer2))
        self.assertEquals(2, network.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(superPeer2 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(not superPeer2 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not superPeer2 in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(superPeer2 in network.getDisconnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        
        superPeer1.leaved()
        
        self.assertEquals(2, network.countPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(superPeer1 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(not superPeer1 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not superPeer1 in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(superPeer1 in network.getDisconnectedPeers(IPeerToPeerNetwork.SUPER_PEER))
        
        simplePeer1 = SimplePeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER), pymockobject.create(IPeerToPeerNetwork))
        simplePeer1.joined()
        
        self.assertTrue(network.addPeer(IPeerToPeerNetwork.SIMPLE_PEER, simplePeer1))
        self.assertEquals(1, network.countPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(simplePeer1 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not simplePeer1 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(simplePeer1 in network.getConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not simplePeer1 in network.getDisconnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        simplePeer2 = SimplePeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER), pymockobject.create(IPeerToPeerNetwork))
        simplePeer2.joined()
        
        self.assertTrue(network.addPeer(IPeerToPeerNetwork.SIMPLE_PEER, simplePeer2))
        self.assertEquals(2, network.countPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(simplePeer2 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not simplePeer2 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(simplePeer2 in network.getConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not simplePeer2 in network.getDisconnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        simplePeer2.leaved()
        
        self.assertEquals(2, network.countPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(simplePeer2 in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(not simplePeer2 in network.getPeers(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(not simplePeer2 in network.getConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        self.assertTrue(simplePeer2 in network.getDisconnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertRaises(TypeError, network.addPeer, "0", pymockobject.create(IPeer))
        self.assertRaises(TypeError, network.addPeer, 0.222, pymockobject.create(IPeer))
        
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, "")
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, 1)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, 1.0)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, True)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, False)
        
        self.assertRaises(InvalidValueError, network.addPeer, IPeerToPeerNetwork.SUPER_PEER, None)
        
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, "")
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1.0)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, True)
        self.assertRaises(TypeError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, False)
        
        self.assertRaises(InvalidValueError, network.addPeer, IPeerToPeerNetwork.SIMPLE_PEER, None)
    
    def testRegisterPeerToPeerProtocol(self):
        simulation = pymockobject.create(ISimulation)
        network = PeerToPeerNetwork(simulation)
        
        protocol1 = pymockobject.create(IPeerToPeerProtocol)
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol1))
        self.assertEquals(protocol1, network.getPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER))
        
        protocol2 = pymockobject.create(IPeerToPeerProtocol)
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, protocol2))
        self.assertEquals(protocol2, network.getPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, "", protocol1)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, 0.88, protocol1)
        
        self.assertRaises(InvalidValueError, network.registerPeerToPeerProtocol, None, protocol1)
        
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, "")
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, 1)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, 0.9)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, True)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, False)
        
        self.assertRaises(InvalidValueError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER, None)
        
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, "")
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, 1)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, 0.9)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, True)
        self.assertRaises(TypeError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, False)
        
        self.assertRaises(InvalidValueError, network.registerPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER, None)
        
    def testUnregisterPeerToPeerProtocol(self):
        simulation = pymockobject.create(ISimulation)
        network = PeerToPeerNetwork(simulation)
        
        protocol1 = pymockobject.create(IPeerToPeerProtocol)
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol1))
        self.assertEquals(protocol1, network.getPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER))
        
        protocol2 = pymockobject.create(IPeerToPeerProtocol)
        self.assertTrue(network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, protocol2))
        self.assertEquals(protocol2, network.getPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertTrue(network.unregisterPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER))
        self.assertTrue(network.unregisterPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER))
        
        self.assertRaises(TypeError, network.unregisterPeerToPeerProtocol, "")
        self.assertRaises(TypeError, network.unregisterPeerToPeerProtocol, 0.7767)
        
        self.assertRaises(InvalidValueError, network.unregisterPeerToPeerProtocol, IPeerToPeerNetwork.SUPER_PEER)
        self.assertRaises(InvalidValueError, network.unregisterPeerToPeerProtocol, IPeerToPeerNetwork.SIMPLE_PEER)