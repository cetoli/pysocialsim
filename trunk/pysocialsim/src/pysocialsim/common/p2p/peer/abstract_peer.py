"""
Defines the module with objective the implementation of AbstractPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import returns
from pysocialsim.common.p2p.topology.graph.node import Node

class AbstractPeer(Object, IPeer):
    """
    Defines the abstract implementation of IPeer interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, type, id, peerToPeerNetwork):
        """
        Initializes the object.
        @param type: the type of peer
        @type type: int
        @param id: the identifier of peer.
        @type id: str
        @param peerToPeerNetwork: the peer-to-peer network
        @type peerToPeerNetwork: IPeerToPeerNetwork 
        """
        self.__id = id
        self.__type = type
        self.__joined = False
        self.__node = None
        self.__peerToPeerNetwork = peerToPeerNetwork
    
    @public    
    def getId(self):
        return returns(self.__id, str)
    
    @public
    def getType(self):
        return returns(self.__type, int)
    
    @public
    def isJoined(self):
        return returns(self.__joined, bool)

    @public
    def isLeaved(self):
        return returns(self.__joined, bool)

    @public
    def joined(self):
        self.__joined = True
        return returns(self.__joined, bool)

    @public
    def leaved(self):
        self.__joined = False
        return returns(self.__joined, bool)
    
    @public
    def getNode(self):
        return returns(self.__node, Node)

    @public
    def setNode(self, node):
        self.__node = node
        return returns(self.__node, Node)

    id = property(getId, None, None, None)

    type = property(getType, None, None, None)

    node = property(getNode, setNode, None, None)
        
    
        