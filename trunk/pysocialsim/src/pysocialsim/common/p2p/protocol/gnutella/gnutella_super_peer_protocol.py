"""
Defines the module with implementation of GnutellaSuperPeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.p2p.protocol.abstract_peer_to_peer_protocol import AbstractPeerToPeerProtocol
from pysocialsim.common.base.decorators import public
from threading import Semaphore
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.peer.i_peer import IPeer
from random import randint
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from sets import ImmutableSet
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage

class GnutellaSuperPeerProtocol(AbstractPeerToPeerProtocol):
    """
    Defines the implementation of peer-to-peer protocol for super peers in gnutella networks.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 20/09/2009
    """

    def __init__(self):
        self.initialize()
    
    def initialize(self):
        AbstractPeerToPeerProtocol.initialize(self)
        self.__peerToPeerMessageHandlers = []

    @public
    def join(self, peer):
        semaphore = Semaphore()
        semaphore.acquire()
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        
        if peer.isJoined():
            semaphore.release()
            return False

        topology = self.getPeerToPeerTopology()
        if topology.countNodes() == 0:
            topology.addNode(peer.getId())
            network = topology.getPeerToPeerNetwork()
            network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).joined()
            network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).setNode(topology.getNode(peer.getId()))
            topology.getNode(peer.getId()).setPeer(peer)
            semaphore.release()
            return topology.hasNode(peer.getId())
        else:
            topology.addNode(peer.getId())
            network = topology.getPeerToPeerNetwork()
            network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).setNode(topology.getNode(peer.getId()))
            topology.getNode(peer.getId()).setPeer(peer)
            aux = False
            if topology.countNodes() > 0:
                network = topology.getPeerToPeerNetwork()
                peers = [n for n in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER) if n.getId() <> peer.getId()]
                for i in range(network.getConnectionsBetweenSuperPeers()):
                    ix = randint(0, len(peers) - 1)
                    neighbor = peers[ix]
                    
                    node = neighbor.getNode()
                    if node.countEdges() < network.getConnectionsBetweenSuperPeers():
                        topology.addEdge(peer.getId(), neighbor.getId())
                        topology.addEdge(neighbor.getId(), peer.getId())
                        network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).joined()
                        aux = network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).isJoined()
                        del peers[ix]
                        if len(peers) == 0:
                            break
                
            semaphore.release()
            return aux

    @public
    def leave(self, peer):
        semaphore = Semaphore()
        semaphore.acquire()
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        pre_condition(peer, lambda x: x.getNode() <> None)
        
        if not peer.isJoined():
            semaphore.release()
            return False
        
        topology = self.getPeerToPeerTopology()
        if topology.countEdges(peer.getNode().getId()) == 0:
            peer.leaved()
            semaphore.release()
            return True
        
        node = peer.getNode()
        edges = ImmutableSet(topology.getEdges(node.getId()))
        for edge in edges:
            targetNode = edge.getTargetNode()
            topology.removeEdge(node.getId(), targetNode.getId())
            topology.removeEdge(targetNode.getId(), node.getId())
        peer.leaved()
        semaphore.release()
        return True
    
    @public
    def send(self, peer, peerToPeerMessage):
        if not peer.hasNeighbor(peerToPeerMessage.getTargetId()):
            return None
        neighbor = peer.getNeighbor(peerToPeerMessage.getTargetId())
        return neighbor.dispatchData(peerToPeerMessage)
    
    @public
    def route(self, peer, peerToPeerMessage):
        semaphore = Semaphore()
        semaphore.acquire()
        
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        
        semaphore.release()
        return True
    
    @public
    def push(self, peer, peerToPeerMessage):
        semaphore = Semaphore()
        semaphore.acquire()
        
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        
        semaphore.release()
        return peerToPeerMessage
    
    @public
    def ping(self, peer, peerToPeerMessage):
        semaphore = Semaphore()
        semaphore.acquire()
        
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        pre_condition(peerToPeerMessage, lambda x: x.getSourceId() <> x.getTargetId())
        
        node = peer.getNode()
        edges = ImmutableSet(self.getPeerToPeerTopology().getEdges(node.getId()))
        for edge in edges:
            edge.dispatchData(peerToPeerMessage)
        
        semaphore.release()
        return peerToPeerMessage
    
    @public
    def pong(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def receive(self, peer, peerToPeerMessage):
        requires(peer, IPeer)
        requires(peerToPeerMessage, IPeerToPeerMessage)
        
        pre_condition(peer, lambda x: x <> None)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        
        peer.receive(peerToPeerMessage)
        
    @public
    def configurePeer(self, peer):
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        
        peer.configure(self.__peerToPeerMessageHandlers)

    