"""
Defines the module with the implementation of GnutellaSimplePeerProtocol.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/10/2009
"""
from pysocialsim.common.p2p.protocol.abstract_peer_to_peer_protocol import AbstractPeerToPeerProtocol
from threading import Semaphore
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.peer.i_peer import IPeer
from random import randint
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.p2p.peer.route import Route
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from sets import ImmutableSet

class GnutellaSimplePeerProtocol(AbstractPeerToPeerProtocol):
    

    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractPeerToPeerProtocol.initialize(self)
        self.__peerToPeerMessageHandlers = []
        self.__peerToPeerMessageHandlers.append(self.PingPeerToPeerMessageHandler())
        self.__peerToPeerMessageHandlers.append(self.PongPeerToPeerMessageHandler())
        self.__peerToPeerMessageHandlers.append(self.RoutePeerToPeerMessageHandler())
        
    @public
    def push(self, peer, peerToPeerMessage):
        return AbstractPeerToPeerProtocol.push(self, peer, peerToPeerMessage)

    @public
    def pull(self, peer, peerToPeerMessage):
        return AbstractPeerToPeerProtocol.pull(self, peer, peerToPeerMessage)

    @public
    def ping(self, peer, peerToPeerMessage):
        return AbstractPeerToPeerProtocol.ping(self, peer, peerToPeerMessage)

    @public
    def pong(self, peer, peerToPeerMessage):
        return AbstractPeerToPeerProtocol.pong(self, peer, peerToPeerMessage)

    @public
    def route(self, peer, peerToPeerMessage):
        sem = Semaphore()
        sem.acquire()
        
        neighbors = peer.getNeighbors()
        routes = []
        for neighbor in neighbors:
            if neighbor.hasRoutes(peerToPeerMessage.getTargetId()):
                rts = neighbor.getRoutes(peerToPeerMessage.getTargetId())
                rt = rts[0]
                for route in rts:
                    if route.getCost() < rt.getCost():
                        rt = route
                routes.append(rt)
                
        route = routes[randint(0, len(routes) - 1)]
        trace = route.getTrace()
        neighbor = peer.getNeighbor(trace[len(trace) - 1])
        message = self.createPeerToPeerMessage(IPeerToPeerProtocol.ROUTE)
        message.init(peerToPeerMessage.getId(), peer.getId(), neighbor.getId(), route.getCost(), peerToPeerMessage.getPriority())
        message.registerParameter("peerToPeerMessage", peerToPeerMessage)
        trace.remove(trace[len(trace) - 1])
        for id in trace:
            message.registerPeerId(id)
        message.registerParameter("backTrace", [peer.getId()])
        neighbor.dispatchData(message)
        
        sem.release()
        return message

    @public
    def join(self, peer):
        sem = Semaphore()
        sem.acquire()
        aux = False
        if peer.isJoined():
            aux = False;
        else:
            topology = self.getPeerToPeerTopology()
            if topology.countNodes() == 0:
                aux = False
            elif topology.countNodes() > 0:
                topology.addNode(peer.getId())
                network = topology.getPeerToPeerNetwork()
                peer.setNode(topology.getNode(peer.getId()))
                peers = [n for n in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER) if n.countChildren() < network.getConnectionsBetweenSuperPeerAndSimplePeers()]
                if len(peers) > 0:
                    for i in range(randint(1, network.getConnectionsBetweenSimplePeerAndSuperPeers())):
                        ix = randint(0, len(peers) - 1)
                        superPeer = peers[ix]
                        if superPeer.countChildren() < network.getConnectionsBetweenSuperPeerAndSimplePeers():
                            topology.addEdge(peer.getId(), superPeer.getId())
                            topology.addEdge(superPeer.getId(), peer.getId())  
                            peer.joined()
                            aux = peer.isJoined();
                            del peers[ix]
                            if len(peers) == 0:
                                break      
        
        sem.release()
        return aux;

    @public
    def leave(self, peer):
        sem = Semaphore()
        sem.acquire()
        aux = False
        if peer.isLeaved():
            aux = False
        else:
            topology = self.getPeerToPeerTopology()
            if topology.countNodes() == 0:
                aux = False
            elif topology.countNodes() > 0:
                node = topology.getNode(peer.getId())
                edges = ImmutableSet(node.getEdges())
                for edge in edges:
                    targetNode = edge.getTargetNode()
                    targetNode.removeEdge(targetNode.getEdge(node.getId()))
                    node.removeEdge(edge)
                topology.removeNode(node.getId())
                peer.setNode(None)
                peer.leaved()
                aux = True
        sem.release()
        return aux


    @public
    def configurePeer(self, peer):
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        
        peer.configure(self.__peerToPeerMessageHandlers)
        
    class PingPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
        
        def __init__(self):
            AbstractPeerToPeerMessageHandler.initialize(self, IPeerToPeerProtocol.PING)
        
        def execute(self):
            message = self.getPeerToPeerMessage()
            
            peer = self.getPeer()
            
            protocol = peer.getPeerToPeerProtocol()
            
            pongMessage = protocol.createPeerToPeerMessage(IPeerToPeerProtocol.PONG)
            pongMessage.registerParameter("backTrace", [peer.getId()])
            
            
            id = PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer)
            sourceId = peer.getId()
            targetId = message.getSourceId()
            ttl = message.getHop()
            priority = message.getPriority()
            
            pongMessage.init(id, sourceId, targetId, ttl, priority, pongMessage.getSize(), pongMessage.getTime())
            for peerId in message.getPeerIds():
                pongMessage.registerPeerId(peerId)
            
            peer.send(pongMessage)
            
            trace = message.getPeerIds()
            if not peer.hasNeighbor(trace[0]):
                route = Route(trace[0], trace, len(trace), 0)
                
                neighbor = peer.getNeighbor(message.getSourceId())
                neighbor.registerRoute(route)
            
    class PongPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
        
        def __init__(self):
            AbstractPeerToPeerMessageHandler.initialize(self, IPeerToPeerProtocol.PONG)
        
        def execute(self):
            message = self.getPeerToPeerMessage()
            peer = self.getPeer()
            
            if peer.getId() == message.getFirst():
                backTrace = message.getParameter("backTrace")
                peerId = backTrace[0]
                route = Route(peerId, backTrace, len(backTrace), 0)
                lastPeerId = backTrace[len(backTrace) - 1]
                if not peer.hasNeighbor(lastPeerId) or peerId == lastPeerId:
                    return
                neighbor = peer.getNeighbor(lastPeerId)
                neighbor.registerRoute(route)
            else:
                print "Deu merda"
        
    class RoutePeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
        
        def __init__(self):
            AbstractPeerToPeerMessageHandler.initialize(self, IPeerToPeerProtocol.ROUTE)
        
        def execute(self):
            print "CCUUUUUUUUUUUUUUUUUUUUUUUUUUU"
        