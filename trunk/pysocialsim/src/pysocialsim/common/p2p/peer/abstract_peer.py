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
from pysocialsim.common.p2p.topology.graph.i_node import INode
from threading import Semaphore
import time

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
        self.__connected = False
        self.__node = None
        self.__peerToPeerNetwork = peerToPeerNetwork
        self.__peerToPeerNetwork.addPeer(self.__type, self)
        self.__peerToPeerProtocol = self.__peerToPeerNetwork.getPeerToPeerProtocol(self.__type)
    
    @public    
    def getId(self):
        return returns(self.__id, str)
    
    @public
    def getType(self):
        return returns(self.__type, int)
    
    @public
    def isJoined(self):
        sem = Semaphore()
        sem.acquire()
        aux = self.__connected
        sem.release()
        return returns(aux == True, bool)

    @public
    def isLeaved(self):
        return returns(self.__connected == False, bool)

    @public
    def joined(self):
        semaphore = Semaphore()
        semaphore.acquire()
        del self.__connected
        self.__connected = True
        semaphore.release()
        return returns(self.__connected, bool)

    @public
    def leaved(self):
        self.__connected = False
        return returns(self.__connected, bool)
    
    @public
    def getNode(self):
        return returns(self.__node, INode)

    @public
    def setNode(self, node):
        sem = Semaphore()
        sem.acquire()
        self.__node = node
        self.__node.setPeer(self.__peerToPeerNetwork.getPeer(self.__type, self.__id))
        sem.release()
        return self.__node
    
    @public
    def join(self):
        aux = self.__peerToPeerProtocol.join(self)
        topology = self.__peerToPeerProtocol.getPeerToPeerTopology()
        self.setNode(topology.getNode(self.__id))
        return aux  
    
    id = property(getId, None, None, None)

    type = property(getType, None, None, None)

    node = property(getNode, setNode, None, None)
        
    
        