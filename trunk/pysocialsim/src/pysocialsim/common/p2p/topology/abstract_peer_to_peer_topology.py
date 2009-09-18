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
from pysocialsim.common.util.rotines import requires, pre_condition

class AbstractPeerToPeerTopology(Object, IPeerToPeerTopology):
    """
    Defines the basic implementation for IPeerToPeerTopology interface
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 18/09/2009
    """

    def initialize(self):
        self.__graph = {}
        self.__peerToPeerNetwork = None
    
    @public
    def addEdge(self, sourceId, targetId):
        requires(sourceId, int)
        requires(targetId, int)
        
        pre_condition(sourceId, lambda x: x > 0)
        pre_condition(targetId, lambda x: x > 0)
        
    @public
    def removeEdge(self, sourceId, targetId):
        pass

    @public
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        self.__peerToPeerNetwork = peerToPeerNetwork
        return self.__peerToPeerNetwork

    @public
    def getPeerToPeerNetwork(self):
        return self.__peerToPeerNetwork