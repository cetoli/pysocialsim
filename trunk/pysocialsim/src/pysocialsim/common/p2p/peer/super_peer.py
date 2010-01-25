"""
Defines the module with the implementation SuperPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.peer.message.superpeer.advertise_opportunity_peer_to_peer_message_handler import AdvertiseOpportunityPeerToPeerMessageHandler

class SuperPeer(AbstractPeer):

    def __init__(self, id, peerToPeerNetwork):
        self.initialize(id, peerToPeerNetwork)

    def initialize(self, id, peerToPeerNetwork):
        AbstractPeer.initialize(self, IPeerToPeerNetwork.SUPER_PEER, id, peerToPeerNetwork)
        dispatcher = self.getPeerToPeerMessageDispatcher()
        dispatcher.registerPeerToPeerMessageHandler(AdvertiseOpportunityPeerToPeerMessageHandler())

    @public
    def countChildren(self):
        neighbors = AbstractPeer.getNeighbors(self)
        count = 0
        for neighbor in neighbors:
            edge = neighbor.getEdge()
            targetNode = edge.getTargetNode()
            peer = targetNode.getPeer()
            if peer.getType() == IPeerToPeerNetwork.SIMPLE_PEER:
                count += 1
        return count
    
    @public
    def countNeighbors(self):
        neighbors = AbstractPeer.getNeighbors(self)
        count = 0
        for neighbor in neighbors:
            edge = neighbor.getEdge()
            targetNode = edge.getTargetNode()
            peer = targetNode.getPeer()
            if peer.getType() == IPeerToPeerNetwork.SUPER_PEER:
                count += 1
        return count

    @public
    def getNeighbors(self):
        neighbors = AbstractPeer.getNeighbors(self)
        count = 0
        lst = []
        for neighbor in neighbors:
            edge = neighbor.getEdge()
            targetNode = edge.getTargetNode()
            peer = targetNode.getPeer()
            if peer.getType() == IPeerToPeerNetwork.SUPER_PEER:
                lst.append(neighbor)
        return lst
    
    @public
    def getChildren(self):
        neighbors = AbstractPeer.getNeighbors(self)
        count = 0
        lst = []
        for neighbor in neighbors:
            edge = neighbor.getEdge()
            targetNode = edge.getTargetNode()
            peer = targetNode.getPeer()
            if peer.getType() == IPeerToPeerNetwork.SIMPLE_PEER:
                lst.append(neighbor)
        return lst
