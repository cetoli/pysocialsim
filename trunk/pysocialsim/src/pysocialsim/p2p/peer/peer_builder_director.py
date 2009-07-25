from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.peer.i_peer_builder import IPeerBuilder
from pysocialsim.base.decorator.public import public
from types import NoneType
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.p2p.protocol.i_p2p_protocol import IP2PProtocol
from pysocialsim.p2p.profile.i_matching_strategy import IMatchingStrategy

class PeerBuilderDirector(Object):
    
    def __init__(self, builder):
        self.initialize(builder)
    
    def initialize(self, builder):
        self.__builder = builder
        self.__totalFile = 0
        self.__builder.setPeerBuilderDirector(self)
    
    @public
    def build(self, params, id, network, protocol, matchingStrategy):
        self.__builder.createPeer(id, network, protocol, matchingStrategy)
        self.__builder.buildContent(params)
    
    @public
    def setTotalFile(self, totalFile):
        self.__totalFile = totalFile
        return self.__totalFile
    
    @public
    def getTotalFile(self):
        return self.__totalFile