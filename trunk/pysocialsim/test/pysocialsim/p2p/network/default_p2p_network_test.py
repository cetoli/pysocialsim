from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
from pysocialsim.p2p.network.default_p2p_network import DefaultP2PNetwork
from pysocialsim.base.interface import implements
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.p2p.peer.i_peer import IPeer
from pymockobject.events import ReturnValue
import pymockobject
import unittest

class DefaultP2PNetworkTest(unittest.TestCase):
    
    def setUp(self):
        self.__topology = pymockobject.create(IP2PTopology)
        self.__network = DefaultP2PNetwork(self.__topology)
        
    def test_implements_interfaces(self):
        self.assertTrue(implements(self.__network, IP2PNetwork))
        
    def test_set_simulation(self):
        simulation = pymockobject.create(ISimulation)
        
        self.assertEquals(simulation, self.__network.setSimulation(simulation)) 
        self.assertEquals(simulation, self.__network.getSimulation())
        
    def test_add_peers(self):
        peer1 = pymockobject.create(IPeer)
        peer1.getId.will(ReturnValue(1))
        
        self.assertEquals(peer1, self.__network.addPeer(peer1))
        self.assertEquals(1, self.__network.countPeers())
        
        peer2 = pymockobject.create(IPeer)
        peer2.getId.will(ReturnValue(2))
        
        self.assertEquals(peer2, self.__network.addPeer(peer2))
        self.assertEquals(2, self.__network.countPeers())
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue(3))
        
        self.assertEquals(peer3, self.__network.addPeer(peer3))
        self.assertEquals(3, self.__network.countPeers())
        
        self.assertRaises(TypeError, self.__network.addPeer, None)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.addPeer, 1)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.addPeer, False)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.addPeer, True)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.addPeer, "peer")
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.addPeer, 0.76)
        self.assertEquals(3, self.__network.countPeers())
        
        self.assertRaises(StandardError, self.__network.addPeer, peer1)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(StandardError, self.__network.addPeer, peer2)
        self.assertEquals(3, self.__network.countPeers())
        self.assertRaises(StandardError, self.__network.addPeer, peer3)
        self.assertEquals(3, self.__network.countPeers())
    
    def test_remove_peers(self):
        peer1 = pymockobject.create(IPeer)
        peer1.getId.will(ReturnValue(1))
        
        self.assertEquals(peer1, self.__network.addPeer(peer1))
        self.assertEquals(1, self.__network.countPeers())
        
        peer2 = pymockobject.create(IPeer)
        peer2.getId.will(ReturnValue(2))
        
        self.assertEquals(peer2, self.__network.addPeer(peer2))
        self.assertEquals(2, self.__network.countPeers())
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue(3))
        
        self.assertEquals(peer3, self.__network.addPeer(peer3))
        self.assertEquals(3, self.__network.countPeers())
        
        self.assertEquals(peer1, self.__network.removePeer(peer1.getId()))
        self.assertEquals(2, self.__network.countPeers())
        
        self.assertEquals(peer2, self.__network.removePeer(peer2.getId()))
        self.assertEquals(1, self.__network.countPeers())
        
        self.assertEquals(peer3, self.__network.removePeer(peer3.getId()))
        self.assertEquals(0, self.__network.countPeers())
        
        self.assertRaises(TypeError, self.__network.removePeer, None)
        self.assertEquals(0, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.removePeer, "1")
        self.assertEquals(0, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.removePeer, False)
        self.assertEquals(0, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.removePeer, True)
        self.assertEquals(0, self.__network.countPeers())
        self.assertRaises(TypeError, self.__network.removePeer, 0.9)
        self.assertEquals(0, self.__network.countPeers())
        
        self.assertRaises(StandardError, self.__network.removePeer, peer1.getId())
        self.assertEquals(0, self.__network.countPeers())
        
        self.assertRaises(StandardError, self.__network.removePeer, peer2.getId())
        self.assertEquals(0, self.__network.countPeers())
        
        self.assertRaises(StandardError, self.__network.removePeer, peer3.getId())
        self.assertEquals(0, self.__network.countPeers())
        
    def test_get_peers(self):
        peer1 = pymockobject.create(IPeer)
        peer1.getId.will(ReturnValue(1))
        
        self.assertEquals(peer1, self.__network.addPeer(peer1))
        self.assertEquals(1, self.__network.countPeers())
        self.assertEquals(peer1, self.__network.getPeer(peer1.getId()))
        
        peer2 = pymockobject.create(IPeer)
        peer2.getId.will(ReturnValue(2))
        
        self.assertEquals(peer2, self.__network.addPeer(peer2))
        self.assertEquals(2, self.__network.countPeers())
        self.assertEquals(peer2, self.__network.getPeer(peer2.getId()))
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue(3))
        
        self.assertEquals(peer3, self.__network.addPeer(peer3))
        self.assertEquals(3, self.__network.countPeers())
        self.assertEquals(peer2, self.__network.getPeer(peer2.getId()))
        
        self.assertEquals(peer1, self.__network.removePeer(peer1.getId()))
        self.assertEquals(2, self.__network.countPeers())
        self.assertRaises(StandardError, self.__network.getPeer, peer1.getId())
        
        self.assertEquals(peer2, self.__network.removePeer(peer2.getId()))
        self.assertEquals(1, self.__network.countPeers())
        self.assertRaises(StandardError, self.__network.getPeer, peer2.getId())
        
        self.assertEquals(peer3, self.__network.removePeer(peer3.getId()))
        self.assertEquals(0, self.__network.countPeers())
        self.assertRaises(StandardError, self.__network.getPeer, peer3.getId())
        
        self.assertRaises(TypeError, self.__network.getPeer, None)
        self.assertRaises(TypeError, self.__network.getPeer, "1")
        self.assertRaises(TypeError, self.__network.getPeer, False)
        self.assertRaises(TypeError, self.__network.getPeer, True)
        self.assertRaises(TypeError, self.__network.getPeer, 0.9)
        
    def test_create_connections(self):
        self.__topology.createConnection.expects(1, 2).will(ReturnValue(True))
        
        peer1 = pymockobject.create(IPeer)
        peer1.getId.will(ReturnValue(1))
        peer1.isConnected.will(ReturnValue(True))
        
        peer2 = pymockobject.create(IPeer)
        peer2.getId.will(ReturnValue(2))
        peer2.isConnected.will(ReturnValue(True))
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue(3))
        peer3.isConnected.will(ReturnValue(False))
        
        self.assertEquals(peer1, self.__network.addPeer(peer1))
        self.assertEquals(peer2, self.__network.addPeer(peer2))
        self.assertEquals(peer3, self.__network.addPeer(peer3))
        
        self.assertTrue(self.__network.createConnection(1, 2))
        
        self.assertRaises(TypeError, self.__network.createConnection, None, 2)
        self.assertRaises(TypeError, self.__network.createConnection, 1, None)
        self.assertRaises(TypeError, self.__network.createConnection, None, None)
        
        self.assertRaises(TypeError, self.__network.createConnection, "1", 2)
        self.assertRaises(TypeError, self.__network.createConnection, 1, "2")
        self.assertRaises(TypeError, self.__network.createConnection, "1", "2")
        
        self.assertRaises(TypeError, self.__network.createConnection, 0.1, 2)
        self.assertRaises(TypeError, self.__network.createConnection, 1, 0.2)
        self.assertRaises(TypeError, self.__network.createConnection, 0.1, 0.2)
        
        self.assertRaises(TypeError, self.__network.createConnection, True, 2)
        self.assertRaises(TypeError, self.__network.createConnection, 1, True)
        self.assertRaises(TypeError, self.__network.createConnection, True, True)
        
        self.assertRaises(TypeError, self.__network.createConnection, False, 2)
        self.assertRaises(TypeError, self.__network.createConnection, 1, False)
        self.assertRaises(TypeError, self.__network.createConnection, False, False)
        
        self.assertRaises(StandardError, self.__network.createConnection, 1, 1)
        
        self.assertRaises(StandardError, self.__network.createConnection, 4, 5)
        self.assertRaises(StandardError, self.__network.createConnection, 5, 4)
        
        self.assertRaises(StandardError, self.__network.createConnection, 1, 3)
        self.assertRaises(StandardError, self.__network.createConnection, 3, 1)
        self.assertRaises(StandardError, self.__network.createConnection, 2, 3)
        self.assertRaises(StandardError, self.__network.createConnection, 3, 2)
        
        self.__topology.isNeighbor.expects(1, 2).will(ReturnValue(True))
        self.assertRaises(StandardError, self.__network.createConnection, 1, 2)
        
    def test_remove_connections(self):
        self.__topology.createConnection.expects(1, 2).will(ReturnValue(True))
        self.__topology.removeConnection.expects(1, 2).will(ReturnValue(True))
        
        peer1 = pymockobject.create(IPeer)
        peer1.getId.will(ReturnValue(1))
        peer1.isConnected.will(ReturnValue(True))
        
        peer2 = pymockobject.create(IPeer)
        peer2.getId.will(ReturnValue(2))
        peer2.isConnected.will(ReturnValue(True))
        
        peer3 = pymockobject.create(IPeer)
        peer3.getId.will(ReturnValue(3))
        peer3.isConnected.will(ReturnValue(False))
        
        self.assertEquals(peer1, self.__network.addPeer(peer1))
        self.assertEquals(peer2, self.__network.addPeer(peer2))
        self.assertEquals(peer3, self.__network.addPeer(peer3))
        
        self.assertTrue(self.__network.createConnection(1, 2))
        self.assertTrue(self.__network.removeConnection(1, 2))
        
        self.assertRaises(TypeError, self.__network.removeConnection, None, 2)
        self.assertRaises(TypeError, self.__network.removeConnection, 1, None)
        self.assertRaises(TypeError, self.__network.removeConnection, None, None)
        
        self.assertRaises(TypeError, self.__network.removeConnection, "1", 2)
        self.assertRaises(TypeError, self.__network.removeConnection, 1, "2")
        self.assertRaises(TypeError, self.__network.removeConnection, "1", "2")
        
        self.assertRaises(TypeError, self.__network.removeConnection, 0.1, 2)
        self.assertRaises(TypeError, self.__network.removeConnection, 1, 0.2)
        self.assertRaises(TypeError, self.__network.removeConnection, 0.1, 0.2)
        
        self.assertRaises(TypeError, self.__network.removeConnection, True, 2)
        self.assertRaises(TypeError, self.__network.removeConnection, 1, True)
        self.assertRaises(TypeError, self.__network.removeConnection, True, True)
        
        self.assertRaises(TypeError, self.__network.removeConnection, False, 2)
        self.assertRaises(TypeError, self.__network.removeConnection, 1, False)
        self.assertRaises(TypeError, self.__network.removeConnection, False, False)

        self.assertRaises(StandardError, self.__network.removeConnection, 1, 1)
        self.assertRaises(StandardError, self.__network.removeConnection, 2, 2)
        
        self.assertRaises(StandardError, self.__network.removeConnection, 4, 5)
        self.assertRaises(StandardError, self.__network.removeConnection, 5, 4)
        
        self.assertRaises(StandardError, self.__network.removeConnection, 1, 5)
        self.assertRaises(StandardError, self.__network.removeConnection, 5, 1)
        self.assertRaises(StandardError, self.__network.removeConnection, 2, 3)
        self.assertRaises(StandardError, self.__network.removeConnection, 3, 2)
        
        self.__topology.isNeighbor.expects(1, 2).will(ReturnValue(False))
        self.assertRaises(StandardError, self.__network.removeConnection, 1, 2)
        