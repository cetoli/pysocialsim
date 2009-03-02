from pysocialsim.network.topology.topology import Topology
from pysocialsim.network.default_network import DefaultNetwork
from pysocialsim.base.interface import implements
from pysocialsim.network.network import Network
from pysocialsim.simulator.simulation.simulation import Simulation
from pymockobject.events import ReturnValue
from pysocialsim.network.peer.peer import Peer
import pymockobject
import unittest

class DefaultNetworkTest(unittest.TestCase):
    
    def test_create_instance(self):
        topology = pymockobject.create(Topology)
        self.assertTrue(DefaultNetwork(topology))
        
        network = DefaultNetwork(topology)
        self.assertEquals(topology, network.getTopology())
        self.assertEquals(None, network.getSimulation())
        self.assertEquals(0, network.countPeers())
        
        self.assertTrue(implements(network, Network))
        
        self.assertRaises(TypeError, DefaultNetwork, None)
        self.assertRaises(TypeError, DefaultNetwork, 1)
        self.assertRaises(TypeError, DefaultNetwork, "str")
        self.assertRaises(TypeError, DefaultNetwork, True)
        self.assertRaises(TypeError, DefaultNetwork, False)
        self.assertRaises(TypeError, DefaultNetwork, 0.589)
        
    def test_set_simulation(self):
        topology = pymockobject.create(Topology)
        simulation = pymockobject.create(Simulation)
        
        network = DefaultNetwork(topology)
        self.assertEquals(simulation, network.setSimulation(simulation))
        self.assertEquals(simulation, network.getSimulation())
        
        self.assertRaises(TypeError, network.setSimulation, None)
        self.assertRaises(TypeError, network.setSimulation, 123)
        self.assertRaises(TypeError, network.setSimulation, 0.2588)
        self.assertRaises(TypeError, network.setSimulation, True)
        self.assertRaises(TypeError, network.setSimulation, False)
        self.assertRaises(TypeError, network.setSimulation, "haha")
        
    def test_generate_events(self):
        topology = pymockobject.create(Topology)
        simulation = pymockobject.create(Simulation)
        
        network = DefaultNetwork(topology)
        
        simulation.countEvents.will(ReturnValue(1000))
        
        self.assertEquals(simulation, network.setSimulation(simulation))
        self.assertEquals(1000, network.generateEvents(simulation))
        
        self.assertRaises(TypeError, network.generateEvents, None)
        self.assertRaises(TypeError, network.generateEvents, 56)
        self.assertRaises(TypeError, network.generateEvents, True)
        self.assertRaises(TypeError, network.generateEvents, False)
        self.assertRaises(TypeError, network.generateEvents, "simulation")
        self.assertRaises(TypeError, network.generateEvents, 0.15487)
        
    def test_add_and_remove_peers(self):
        topology = pymockobject.create(Topology)
        network = DefaultNetwork(topology)
        
        peer1 = pymockobject.create(Peer)
        peer1.getId.will(ReturnValue(1))
        self.assertEquals(peer1, network.addPeer(peer1))
        self.assertEquals(None, network.addPeer(peer1))
        self.assertEquals(peer1, network.getPeer(1))
        self.assertEquals(1, network.countPeers())
        
        peer2 = pymockobject.create(Peer)
        peer2.getId.will(ReturnValue(30))
        self.assertEquals(peer2, network.addPeer(peer2))
        self.assertEquals(None, network.addPeer(peer2))
        self.assertEquals(peer2, network.getPeer(30))
        self.assertEquals(2, network.countPeers())
        
        peer3 = pymockobject.create(Peer)
        peer3.getId.will(ReturnValue(123))
        self.assertEquals(peer3, network.addPeer(peer3))
        self.assertEquals(None, network.addPeer(peer3))
        self.assertEquals(peer3, network.getPeer(123))
        self.assertEquals(3, network.countPeers())
        
        self.assertRaises(TypeError, network.addPeer, None)
        self.assertRaises(TypeError, network.addPeer, "peer")
        self.assertRaises(TypeError, network.addPeer, 123)
        self.assertRaises(TypeError, network.addPeer, True)
        self.assertRaises(TypeError, network.addPeer, False)
        self.assertRaises(TypeError, network.addPeer, 0.125)
        
        self.assertEquals(peer1, network.removePeer(1))
        self.assertEquals(None, network.removePeer(1))
        self.assertEquals(None, network.getPeer(1))
        self.assertEquals(2, network.countPeers())
        
        self.assertEquals(peer1, network.removePeer(30))
        self.assertEquals(None, network.removePeer(30))
        self.assertEquals(None, network.getPeer(30))
        self.assertEquals(1, network.countPeers())
        
        self.assertEquals(peer1, network.removePeer(123))
        self.assertEquals(None, network.removePeer(123))
        self.assertEquals(None, network.getPeer(123))
        self.assertEquals(0, network.countPeers())
        
        self.assertRaises(TypeError, network.removePeer, None)
        self.assertRaises(TypeError, network.removePeer, "1")
        self.assertRaises(TypeError, network.removePeer, peer1)
        self.assertRaises(TypeError, network.removePeer, 0.2356)