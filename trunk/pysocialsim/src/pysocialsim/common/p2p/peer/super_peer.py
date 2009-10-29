"""
Defines the module with the implementation SuperPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.i_super_peer import ISuperPeer

class SuperPeer(AbstractPeer, ISuperPeer):

    def __init__(self, id, peerToPeerNetwork):
        AbstractPeer.initialize(self, IPeerToPeerNetwork.SUPER_PEER, id, peerToPeerNetwork)

    def countChildren(self):
        neighbors = self.getNeighbors()
        count = 0
        for neighbor in neighbors:
            edge = neighbor.getEdge()
            targetNode = edge.getTargetNode()
            peer = targetNode.getPeer()
            if peer.getType() == IPeerToPeerNetwork.SIMPLE_PEER:
                count += 1
        return count