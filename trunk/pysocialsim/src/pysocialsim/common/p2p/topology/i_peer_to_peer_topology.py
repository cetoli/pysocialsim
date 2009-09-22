"""
Defines the module with the specification of IPeerToPeerTopology interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/09/2009
"""
class IPeerToPeerTopology(object):
    """
    Defines the operations of peer-to-peer topology.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 15/09/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def addEdge(self, sourceId, targetId):
        """
        Creates a connection between two peers.
        @param sourceId: the identifier of source peer
        @type sourceId: int
        @param targetId: the identifier of target peer
        @type targetId: int
        @return: If connection was created, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def removeEdge(self, sourceId, targetId):
        """
        Removes a connection between two peers.
        @param sourceId: the identifier of source peer
        @type sourceId: int
        @param targetId: the identifier of target peer
        @type targetId: int
        @return: If connection was removed, returns True. Else, returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def getEdge(self, sourceId, targetId):
        """
        Gets a edge.
        @param sourceId: the identifier of source node
        @type sourceId: int
        @param targetId: the identifier of target node
        @type targetId: int
        @return: an IEdge
        @rtype: IEdge
        """
        raise NotImplementedError()
    
    def getEdges(self, nodeId):
        """
        Gets the list of edges in node
        @param nodeId: the identifier of node
        @type nodeId: int
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def countEdges(self, nodeId):
        """
        Counts the number of edges in node
        @param nodeId: the identifier of node
        @type nodeId: int
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        """
        Sets the peer-to-peer network.
        @param peerToPeerNetwork: an IPeerToPeerNetwork
        @type peerToPeerNetwork: IPeerToPeerNetwork
        @return: an IPeerToPeerNetwork
        @rtype: IPeerToPeerNetwork
        """
        raise NotImplementedError()
    
    def getPeerToPeerNetwork(self):
        """
        Gets the peer-to-peer network.
        @return: an IPeerToPeerNetwork
        @rtype: IPeerToPeerNetwork
        """
        raise NotImplementedError()
    
    def addNode(self, nodeId):
        """
        Adds a node in topology.
        @param nodeId: the node identifier
        @type nodeId: int
        @return: If node was registered, returns True, else returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def removeNode(self, nodeId):
        """
        Adds a node in topology.
        @param nodeId: the node identifier
        @type nodeId: int
        @return: If node was removed, returns True, else returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def getNode(self, nodeId):
        """
        Gets a node in topology.
        @param nodeId: the node identifier
        @type nodeId: int
        @return: a Node
        @rtype: Node
        """
        raise NotImplementedError()
    
    def getNodes(self):
        """
        Gets the list of node
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def countNodes(self):
        """
        Counts the number of nodes.
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getNeighbors(self, nodeId):
        """
        Gets the neighbors of node
        @return: a list
        @rtype: list
        """
        raise NotImplementedError()
    
    def hasNode(self, nodeId):
        raise NotImplementedError()
    
    def hasEdge(self):
        raise NotImplementedError()