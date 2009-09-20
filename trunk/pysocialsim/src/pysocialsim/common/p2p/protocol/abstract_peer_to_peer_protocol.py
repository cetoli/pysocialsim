"""
Defines the module with the implementation of AbstractPeerToPeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology

class AbstractPeerToPeerProtocol(Object, IPeerToPeerProtocol):
    """
    Defines the abstract implementation of IPeerToPeerProtocol interface
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 20/09/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__peerToPeerTopology = None

    @public
    def setPeerToPeerTopology(self, peerToPeerTopology):
        requires(peerToPeerTopology, IPeerToPeerTopology)
        pre_condition(peerToPeerTopology, lambda x: x <> None)
        
        self.__peerToPeerTopology = peerToPeerTopology
        
        return returns(self.__peerToPeerTopology, IPeerToPeerTopology)

    @public
    def getPeerToPeerTopology(self):
        return returns(self.__peerToPeerTopology, IPeerToPeerTopology)