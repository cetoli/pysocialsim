"""
Defines the module with the implementation of AbstractNeighbor class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.i_neighbor import INeighbor
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.p2p.peer.i_route import IRoute
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.p2p.topology.graph.i_edge import IEdge

class AbstractNeighbor(Object, INeighbor):
    """
    Defines the common implementation of INeighbor interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/10/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, peer, edge):
        requires(peer, IPeer)
        requires(edge, IEdge)
        self.__peer = peer
        self.__edge = edge
        self.__routes = {}

    @public
    def getId(self):
        return returns(self.__edge.getTargetNode().getId(), str)

    @public
    def getEdge(self):
        return returns(self.__edge, IEdge)

    @public
    def getPeer(self):
        return returns(self.__peer, IPeer)

    @public
    def dispatchData(self, data):
        return self.__edge.dispatchData(data)
    
    @public
    def registerRoute(self, route):
        requires(route, IRoute)
        pre_condition(route, lambda x: x <> None)
        
        if not self.__routes.has_key(route.getPeerId()):
            self.__routes[route.getPeerId()] = []
        
        if not route in self.__routes[route.getPeerId()]:
            self.__routes[route.getPeerId()].append(route)
            print self.getId(),  route.getPeerId()
            #print 22222222222222222222222222222222222
                    
        return returns(self.__routes.has_key(route.getPeerId()), bool)

    @public
    def unregisterRoute(self, peerId):
        return INeighbor.unregisterRoute(self, peerId)

    @public
    def countRoutes(self, peerId):
        if not self.__routes.has_key(peerId):
            return 0
        return returns(len(self.__routes[peerId]), int)

    @public
    def getRoutes(self, peerId):
        if not self.__routes.has_key(peerId):
            return []
        return self.__routes[peerId]
    
    @public
    def hasRoutes(self, peerId):
        if not self.__routes.has_key(peerId):
            return False
        return returns(len(self.__routes[peerId]) > 0, bool)


    
    
        