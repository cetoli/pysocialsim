"""
Defines the module with the unit test of IPeerToPeerNetwork interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class IPeerToPeerNetworkTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerNetwork)
        
    def testTryInvokeGetSimulation(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getSimulation)
    
    def testTryInvokeSetSimulation(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().setSimulation, pymockobject.create(ISimulation))
    
    def testTryInvokeAddPeer(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().addPeer, IPeerToPeerNetwork.SUPER_PEER, pymockobject.create(IPeer))
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().addPeer, IPeerToPeerNetwork.SIMPLE_PEER, pymockobject.create(IPeer))
        
    def testTryInvokeGetPeer(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeer, IPeerToPeerNetwork.SUPER_PEER, 10) 
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1)
        
    def testTryInvokeRemovePeer(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().removePeer, IPeerToPeerNetwork.SUPER_PEER, 10) 
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().removePeer, IPeerToPeerNetwork.SIMPLE_PEER, 1)
        
    def testTryGetPeers(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeers, IPeerToPeerNetwork.SIMPLE_PEER)
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeers, IPeerToPeerNetwork.SUPER_PEER)
    
    def testTryCountPeers(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().countPeers, IPeerToPeerNetwork.SIMPLE_PEER)
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().countPeers, IPeerToPeerNetwork.SUPER_PEER)
    
    def testTryGetConnectedPeers(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getConnectedPeers, IPeerToPeerNetwork.SIMPLE_PEER)
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getConnectedPeers, IPeerToPeerNetwork.SUPER_PEER)
        
    def testTryGetDisconnectedPeers(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getDisconnectedPeers, IPeerToPeerNetwork.SIMPLE_PEER)
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getDisconnectedPeers, IPeerToPeerNetwork.SUPER_PEER)
        
    
    
    class PeerToPeerNetworkForTest(IPeerToPeerNetwork):
        
        def __init__(self):
            pass