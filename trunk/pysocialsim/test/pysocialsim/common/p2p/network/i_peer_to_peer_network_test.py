"""
Defines the module with the unit test of IPeerToPeerNetwork interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

class IPeerToPeerNetworkTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerNetwork)
        
    def testTryInvokeGetSimulation(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getSimulation)
    
    def testTryInvokeSetSimulation(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().setSimulation, pymockobject.create(ISimulation))
        
    def testTryInvokeGetPeer(self):
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeer, IPeerToPeerNetwork.SUPER_PEER, 10) 
        self.assertRaises(NotImplementedError, self.PeerToPeerNetworkForTest().getPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1)
    
    class PeerToPeerNetworkForTest(IPeerToPeerNetwork):
        
        def __init__(self):
            pass