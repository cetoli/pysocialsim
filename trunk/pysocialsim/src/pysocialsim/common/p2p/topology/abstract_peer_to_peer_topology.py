"""
Defines the module with the implementation AbstractPeerToPeerTopology class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.topology.graph.node import Node
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.topology.graph.edge import Edge
from pysocialsim.common.p2p.topology.graph.i_edge import IEdge
from threading import Semaphore

class AbstractPeerToPeerTopology(Object, IPeerToPeerTopology):
    """
    Defines the basic implementation for IPeerToPeerTopology interface
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 18/09/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self):
        self.__graph = {}
        self.__peerToPeerNetwork = None
    
    @public
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        requires(peerToPeerNetwork, IPeerToPeerNetwork)
        pre_condition(peerToPeerNetwork, lambda x: x <> None)
        
        self.__peerToPeerNetwork = peerToPeerNetwork
        return self.__peerToPeerNetwork

    @public
    def getPeerToPeerNetwork(self):
        return returns(self.__peerToPeerNetwork, IPeerToPeerNetwork)
    
    @public
    def addEdge(self, sourceId, targetId):
        requires(sourceId, str)
        requires(targetId, str)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(sourceId))
        pre_condition(targetId, lambda x: self.__graph.has_key(targetId))
        
        semaphore = Semaphore()
        semaphore.acquire()
        node = self.__graph[sourceId]
        if node.hasEdge(targetId):
            return False
        targetNode = self.__graph[targetId]
        node = self.__graph[sourceId]
        edge = Edge(node, targetNode)
        node.addEdge(edge)
        semaphore.release()
        return returns(node.hasEdge(targetId), bool)
        

    @public
    def removeEdge(self, sourceId, targetId):
        requires(sourceId, str)
        requires(targetId, str)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(sourceId))
        pre_condition(targetId, lambda x: self.__graph[sourceId].hasEdge(x))
        
        semaphore = Semaphore()
        semaphore.acquire()
        rtrn = returns(self.__graph[sourceId].removeEdge(self.__graph[sourceId].getEdge(targetId)), bool)
        semaphore.release()
        return rtrn
        
    @public
    def addNode(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        
        semaphore = Semaphore()
        semaphore.acquire()
        if self.__graph.has_key(nodeId):
            return False
        node = Node(nodeId, self)
        self.__graph[node.getId()] = node
        semaphore.release()
        return returns(self.__graph.has_key(node.getId()), bool)

    @public
    def removeNode(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        
        semaphore = Semaphore()
        semaphore.acquire()
        if not self.__graph.has_key(nodeId):
            return False
        
        node = self.__graph[nodeId]
        
        if node.getPeer():
            peer = node.getPeer()
            peer.setNode(None)
        
        del self.__graph[nodeId]
        semaphore.release()
        return returns(not self.__graph.has_key(nodeId), bool)

    @public
    def getNode(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        semaphore = Semaphore()
        semaphore.acquire()
        rtnr = returns(self.__graph[nodeId], INode)
        semaphore.release()
        return rtnr

    @public
    def getNodes(self):
        semaphore = Semaphore()
        semaphore.acquire()
        rtrn = self.__graph.itervalues()
        semaphore.release()
        return rtrn

    @public
    def countNodes(self):
        semaphore = Semaphore()
        semaphore.acquire()
        rtrn = returns(len(self.__graph), int)
        semaphore.release()
        return rtrn
    @public
    def getEdge(self, sourceId, targetId):
        requires(sourceId, str)
        requires(targetId, str)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(x))
        pre_condition(targetId, lambda x: self.__graph[sourceId].hasEdge(x))
        
        semaphore = Semaphore()
        semaphore.acquire()
        rtrn = returns(self.__graph[sourceId].getEdge(targetId), IEdge)
        semaphore.release()
        return rtrn
    
    @public
    def getEdges(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(x))
        
        semaphore = Semaphore()
        semaphore.acquire()
        rtrn = self.__graph[nodeId].getEdges()
        semaphore.release()
        return rtrn

    @public
    def countEdges(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        semaphore = Semaphore()
        semaphore.acquire()
        node = self.__graph[nodeId]
        rtrn = returns(node.countEdges(), int)
        semaphore.release()
        return rtrn
    
    @public
    def getAdjacentNodes(self, nodeId):
        requires(nodeId, str)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        semaphore = Semaphore()
        semaphore.acquire()
        neighbors = []
        for edge in self.__graph[nodeId].getEdges():
            neighbors.append(edge.getTargetNode())
        rtrn = neighbors.__iter__()
        semaphore.release()
        return rtrn
    
    @public
    def hasNode(self, nodeId):
        requires(nodeId, str)
        pre_condition(nodeId, lambda x: x <> None)
        return returns(self.__graph.has_key(nodeId), bool)
    
    @public
    def hasEdge(self, sourceId, targetId):
        requires(sourceId, str)
        pre_condition(sourceId, lambda x: x <> None)
        requires(targetId, str)
        pre_condition(targetId, lambda x: x <> None)
        
        return returns(self.__graph[sourceId].hasEdge(targetId), bool)