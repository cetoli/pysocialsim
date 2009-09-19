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
        requires(sourceId, int)
        requires(targetId, int)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(sourceId))
        pre_condition(targetId, lambda x: self.__graph.has_key(targetId))
        
        node = self.__graph[sourceId]
        if node.hasEdge(targetId):
            return False
        targetNode = self.__graph[targetId]
        edge = Edge(targetNode)
        node.addEdge(edge)
        return returns(node.hasEdge(targetId), bool)
        

    @public
    def removeEdge(self, sourceId, targetId):
        requires(sourceId, int)
        requires(targetId, int)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(sourceId))
        pre_condition(targetId, lambda x: self.__graph[sourceId].hasEdge(x))
        
        return returns(self.__graph[sourceId].removeEdge(self.__graph[sourceId].getEdge(targetId)), bool)
        
    @public
    def addNode(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        
        if self.__graph.has_key(nodeId):
            return False
        node = Node(nodeId, self)
        self.__graph[node.getId()] = node
        return returns(self.__graph.has_key(node.getId()), bool)

    @public
    def removeNode(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        
        if not self.__graph.has_key(nodeId):
            return False
        
        del self.__graph[nodeId]
        return returns(not self.__graph.has_key(nodeId), bool)

    @public
    def getNode(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        return returns(self.__graph[nodeId], INode)

    @public
    def getNodes(self):
        return self.__graph.itervalues()

    @public
    def countNodes(self):
        return returns(len(self.__graph), int)
    
    @public
    def getEdge(self, sourceId, targetId):
        requires(sourceId, int)
        requires(targetId, int)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        pre_condition(sourceId, lambda x: x <> None)
        pre_condition(targetId, lambda x: x <> None)
        pre_condition(sourceId, lambda x: self.__graph.has_key(x))
        pre_condition(targetId, lambda x: self.__graph[sourceId].hasEdge(x))
        
        return returns(self.__graph[sourceId].getEdge(targetId), IEdge)

    @public
    def getEdges(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(x))
        
        return self.__graph[nodeId].getEdges()

    @public
    def countEdges(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        node = self.__graph[nodeId]
        return returns(node.countEdges(), int)
    
    @public
    def getNeighbors(self, nodeId):
        requires(nodeId, int)
        
        pre_condition(nodeId, lambda x: x > 0)
        pre_condition(nodeId, lambda x: x <> None)
        pre_condition(nodeId, lambda x: self.__graph.has_key(nodeId))
        
        neighbors = []
        for edge in self.__graph[nodeId].getEdges():
            neighbors.append(edge.getTargetNode())
        
        return neighbors.__iter__()