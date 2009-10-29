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
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.peer.route import Route

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
        self.__peerToPeerMessageHandlers.append(self.PingPeerToPeerMessageHandler())
        self.__peerToPeerMessageHandlers.append(self.PongPeerToPeerMessageHandler())
        self.__peerToPeerMessageHandlers.append(self.RoutePeerToPeerMessageHandler())

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
            network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).joined()
            network.getPeer(IPeerToPeerNetwork.SUPER_PEER, peer.getId()).setNode(topology.getNode(peer.getId()))
            topology.getNode(peer.getId()).setPeer(peer)
            aux = False
            if topology.countNodes() > 0:
                network = topology.getPeerToPeerNetwork()
                peers = [n for n in network.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER) if (n.getId() <> peer.getId()) and (n.countNeighbors() < network.getConnectionsBetweenSuperPeers())]
                if len(peers) > 0:
                    for i in range(randint(1, network.getConnectionsBetweenSuperPeers())):
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
                    aux = True
                
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
    def route(self, peer, peerToPeerMessage):
        semaphore = Semaphore()
        semaphore.acquire()
        message = None
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        
        if peerToPeerMessage.getHandle() == IPeerToPeerProtocol.ROUTE:
            peerToPeerMessage.unregisterPeerId(peer.getId())
            peerId = peerToPeerMessage.getLast()
            if peer.hasNeighbor(peerId):
                message = peerToPeerMessage.clone()
                message.getParameter("backTrace").append(peer.getId())
                
                message.setHop(message.getHop() + 1)
                message.init(message.getId(), peer.getId(), peerId, message.getTTL(), message.getPriority())
                peer.send(message)
            else:
                raise StandardError("OLHA AQUI, DEU ERRO")
        else:
            neighbors = peer.getNeighbors()
            routes = []
            print peer.getId()
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
        semaphore.release()
        
        return message
    
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
            
            pongMessage.init(id, sourceId, targetId, ttl, priority)
            for peerId in message.getPeerIds():
                pongMessage.registerPeerId(peerId)
            
            peer.send(pongMessage)
            
            if message.getHop() + 1 == message.getTTL():
                return
            
            if message.countPeerIds() == peer.countNeighbors():
                return
            
            if message.getHop() < message.getTTL():
                
                for neighbor in peer.getNeighbors():
                    if message.hasPeerId(neighbor.getId()):
                        continue

                    msgClone = message.clone()
                    msgClone.init(message.getId(), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority())
                    msgClone.setHop(message.getHop() + 1)
                    msgClone.registerPeerId(peer.getId())
                    neighbor.dispatchData(msgClone)
                    
            
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
                message.unregisterPeerId(peer.getId())
                peerId = message.getLast()
                
                if not peer.hasNeighbor(peerId):
                    return
                
                cloneMsg = message.clone()
                cloneMsg.getParameter("backTrace").append(peer.getId())
                
                cloneMsg.setHop(message.getHop() + 1)
                cloneMsg.init(message.getId(), peer.getId(), peerId, message.getTTL(), message.getPriority())
                
                neighbor = peer.getNeighbor(peerId)
                neighbor.dispatchData(cloneMsg)                
    
    class RoutePeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
        
        def __init__(self):
            AbstractPeerToPeerMessageHandler.initialize(self, IPeerToPeerProtocol.ROUTE)
            
        def execute(self):
            message = self.getPeerToPeerMessage()
            peer = self.getPeer()
            
            if peer.getId() == message.getFirst():
                peerToPeerMessage = message.getParameter("peerToPeerMessage")
                dispatcher = peer.getPeerToPeerMessageDispatcher()
                dispatcher.registerPeerToPeerMessage(peerToPeerMessage)
            else:
                peer.route(message)