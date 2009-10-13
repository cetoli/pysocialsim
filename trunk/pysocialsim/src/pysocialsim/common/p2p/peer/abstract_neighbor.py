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
        self.__peer = peer
        self.__edge = edge

    @public
    def getId(self):
        return self.__edge.getTargetNode().getId()

    @public
    def getEdge(self):
        return self.__edge

    @public
    def getPeer(self):
        return self.__peer

    @public
    def dispatchData(self, data):
        return self.__edge.dispatchData(data)

    
    
        