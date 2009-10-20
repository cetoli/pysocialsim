"""
Defines the module with the implementation of Route class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/10/2009
"""
from pysocialsim.common.p2p.peer.abstract_route import AbstractRoute

class Route(AbstractRoute):

    def __init__(self, peerId, trace, cost, freshness):
        AbstractRoute.initialize(self, peerId, trace, cost, freshness)
        