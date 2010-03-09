"""
Defines the module with the specification of INeighbor class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/10/2009
"""

class INeighbor(object):
    """
    Defines operations of neighbors.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/10/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        """
        Gets the identifier of neighbor.
        @return: a str
        @rtype: str
        """
        raise NotImplementedError()
    
    def getEdge(self):
        """
        Gets the edge of adjacent node.
        @return: an IEdge
        @rtype: IEdge
        """
        raise NotImplementedError()
    
    def getPeer(self):
        """
        Gets the owner peer of edge.
        @return: an IPeer
        @rtype: IPeer
        """
        raise NotImplementedError()
    
    def dispatchData(self, data):
        raise NotImplementedError()
    
    
    def registerRoute(self, route):
        raise NotImplementedError()
    
    def unregisterRoute(self, peerId):
        raise NotImplementedError()
    
    def countRoutes(self, peerId):
        raise NotImplementedError()
    
    def getRoutes(self):
        raise NotImplementedError()
    
    def hasRoutes(self, peerId):
        raise NotImplementedError()