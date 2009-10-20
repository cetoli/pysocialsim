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
from pysocialsim.common.util.rotines import returns, requires, pre_condition
from pysocialsim.common.p2p.topology.graph.i_node import INode
from threading import Semaphore
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.message.peer_to_peer_message_dispatcher import PeerToPeerMessageDispatcher

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
        self.__neighbors = {}
        self.__peerToPeerMessageDispatcher = PeerToPeerMessageDispatcher(self)
        self.__peerToPeerProtocol.configurePeer(self)
    
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
        self.__connected = True
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
        sem.release()
        return self.__node
    
    @public
    def join(self):
        aux = self.__peerToPeerProtocol.join(self)
        topology = self.__peerToPeerProtocol.getPeerToPeerTopology()
        self.setNode(topology.getNode(self.__id))
        simulation = self.__peerToPeerNetwork.getSimulation()
        if len(self.__neighbors) > 0:
            for n in self.__neighbors.values():
                message = self.__peerToPeerProtocol.createPeerToPeerMessage(IPeerToPeerProtocol.PING)
                message.registerPeerId(self.__id)
                messageId = PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(self)           
                message.init(messageId, self.__id, n.getId(), len(self.__peerToPeerNetwork.getConnectedPeers(IPeerToPeerNetwork.SUPER_PEER)) - 1, simulation.getCurrentSimulationTime())
                self.send(message)
        return aux
    
    @public
    def receive(self, peerToPeerMessage):
        return self.__peerToPeerMessageDispatcher.handlePeerToPeerMessage(peerToPeerMessage)
    
    @public
    def send(self, peerToPeerMessage):
        return self.__peerToPeerProtocol.send(self, peerToPeerMessage)  
    
    @public
    def getPeerToPeerNetwork(self):
        return self.__peerToPeerNetwork
    
    def __eq__(self, other):
        requires(other, IPeer)
        pre_condition(other, lambda x: x <> None)
        return self.__id == other.getId()
    
    @public
    def addNeighbor(self, neighbor):
        self.__neighbors[neighbor.getId()] = neighbor
        return self.__neighbors.has_key(neighbor.getId())
    
    @public
    def countNeighbors(self):
        return len(self.__neighbors)
    
    @public
    def hasNeighbor(self, peerId):
        return self.__neighbors.has_key(peerId)
    
    @public
    def getNeighbor(self, peerId):
        return self.__neighbors[peerId]
    
    @public
    def getPeerToPeerProtocol(self):
        return self.__peerToPeerProtocol
    
    @public
    def configure(self, peerToPeerMessageHandlers):
        numHandlers = 0
        for handler in peerToPeerMessageHandlers:
            self.__peerToPeerMessageDispatcher.registerPeerToPeerMessageHandler(handler)
            numHandlers += 1
        return numHandlers
    
    @public
    def getNeighbors(self):
        return self.__neighbors.values()
    
    id = property(getId, None, None, None)

    type = property(getType, None, None, None)

    node = property(getNode, setNode, None, None)

    peerToPeerNetwork = property(getPeerToPeerNetwork, None, None, None)

    peerToPeerProtocol = property(getPeerToPeerProtocol, None, None, None)
        
    
        