"""
Defines the module with the unit test of GnutellaSuperPeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.p2p.protocol.gnutella.gnutella_super_peer_protocol import GnutellaSuperPeerProtocol
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.p2p.topology.graph.node import Node
import pymockobject

import unittest

class GnutellaSuperPeerProtocolTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(GnutellaSuperPeerProtocol())
        protocolo = GnutellaSuperPeerProtocol()
        self.assertFalse(protocolo.getPeerToPeerTopology())
        
    def testJoinSuperPeerInGnutellaNetwork(self):
        protocolo = GnutellaSuperPeerProtocol()
        
        peer = pymockobject.create(IPeer)
        peer.isJoined.will(ReturnValue(False))
        peer.getId.will(ReturnValue(12))
        
        topology = pymockobject.create(IPeerToPeerTopology)
        topology.countNodes.will(ReturnValue(0))
        topology.addNode.expects(12).will(ReturnValue(True))
        node = Node(12, topology)
        topology.getNode.expects(12).will(ReturnValue(node))
        peer.setNode.expects(node).will(ReturnValue(node))
        
        protocolo.setPeerToPeerTopology(topology)
        
        self.assertTrue(protocolo.join(peer))
        
        peer = pymockobject.create(IPeer)
        peer.isJoined.will(ReturnValue(True))
        
        self.assertFalse(protocolo.join(peer))
        
        peer = pymockobject.create(IPeer)
        peer.isJoined.will(ReturnValue(False))
        
        