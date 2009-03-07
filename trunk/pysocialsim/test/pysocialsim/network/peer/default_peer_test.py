from pysocialsim.network.network import Network
from pysocialsim.network.peer.default_peer import DefaultPeer
from pysocialsim.base.interface import implements
from pysocialsim.network.peer.peer import Peer
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator
from pysocialsim.simulator.simulation.simulation import Simulation
from pymockobject.events import ReturnValue
from pysocialsim.network.topology.topology import Topology
import pymockobject
import unittest

class DefaultPeerTest(unittest.TestCase):
    
    def test_create_instance(self):
        network = pymockobject.create(Network)
        self.assertTrue(DefaultPeer(1, network, 10, 1))
        self.assertTrue(implements(DefaultPeer(1, network, 10, 1), Peer))
        
        peer = DefaultPeer(1, network, 10, 1)
        self.assertEquals(1, peer.getId())
        self.assertEquals(network, peer.getNetwork())
        self.assertEquals(0, peer.countEventGenerators())
        self.assertFalse(peer.isConnected())
        
        self.assertRaises(TypeError, DefaultPeer, 12, None, 10, 1)
        self.assertRaises(TypeError, DefaultPeer, None, network, 10, 1)
        self.assertRaises(TypeError, DefaultPeer, None, None, 10, 1)
        self.assertRaises(TypeError, DefaultPeer, "12", "123", 10, 1)
    
    def test_add_event_generator(self):
        network = pymockobject.create(Network)
        simulation = pymockobject.create(Simulation)
        peer = DefaultPeer(12, network, 10, 1)
        
        generator1 = pymockobject.create(EventGenerator)
        generator1.generateEvents.expects(simulation).will(ReturnValue(5000))
        
        self.assertEquals(generator1, peer.addEventGenerator(generator1))
    
    def test_connect_and_disconnect_peer(self):
        network = pymockobject.create(Network)
        topology = pymockobject.create(Topology)
        
        peer = DefaultPeer(15, network, 10, 1);
        
        network.getTopology.will(ReturnValue(topology))
        topology.connect.expects(peer)
        topology.disconnect.expects(peer)
        
        peer.connect()
        self.assertTrue(peer.isConnected())
        peer.disconnect()
        self.assertFalse(peer.isConnected())
        
    
