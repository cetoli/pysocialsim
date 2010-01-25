"""
Defines the module with the implementation of Neighbor class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/10/2009
"""
from pysocialsim.common.p2p.peer.abstract_neighbor import AbstractNeighbor

class Neighbor(AbstractNeighbor):
    """
    Defines the concrete implementation of INeighbor.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/10/2009
    """

    def __init__(self, peer, edge):
        AbstractNeighbor.initialize(self, peer, edge)
        