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
from pysocialsim.common.p2p.message.peer_to_peer_message_dispatcher import PeerToPeerMessageDispatcher
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from pysocialsim.common.p2p.peer.i_neighbor import INeighbor
from pysocialsim.common.p2p.peer.context.context_manager import ContextManager
from pysocialsim.common.p2p.peer.profile.social_profile import SocialProfile
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.sharing.disk_sharing import DiskSharing
from pysocialsim.common.p2p.peer.sharing.HardwareSharingIdGenerator import HardwareSharingIdGenerator
from pysocialsim.common.p2p.peer.sharing.memory_sharing import MemorySharing
from pysocialsim.common.p2p.peer.sharing.processor_sharing import ProcessorSharing

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
        requires(type, int)
        requires(id, str)
        requires(peerToPeerNetwork, IPeerToPeerNetwork)
        
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
        self.__contextManager = ContextManager(self)
        self.__socialProfile = SocialProfile(self)
        self.__joinTime = 0
        self.__hardwareSharings = {INode.DISK: {}, INode.MEMORY: {}, INode.PROCESSOR: {}}
    
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
        if self.__node:
            self.__node.setPeer(self)
        sem.release()
        return returns(self.__node, INode)
    
    @public
    def join(self, priority):
        aux = self.__peerToPeerProtocol.join(self)
        if aux:
            self.joined()
            self.__peerToPeerMessageDispatcher.on()
            if len(self.__neighbors) > 0:
                for n in self.__neighbors.values():
                    message = self.__peerToPeerProtocol.createPeerToPeerMessage(IPeerToPeerProtocol.PING)
                    message.registerPeerId(self.__id)
                    messageId = PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(self)           
                    message.init(messageId, self.__id, n.getId(), self.__peerToPeerProtocol.getPingHops(), priority, message.getSize(), message.getTime())
                    self.send(message)
        
        return returns(aux, bool)
    
    @public
    def leave(self, priority):
        self.__peerToPeerMessageDispatcher.off()
        aux = self.__peerToPeerProtocol.leave(self)
        
        return returns(aux, bool)
    @public
    def receive(self, peerToPeerMessage):
        return returns(self.__peerToPeerMessageDispatcher.registerPeerToPeerMessage(peerToPeerMessage), IPeerToPeerMessage)
    
    @public
    def send(self, peerToPeerMessage):
        return returns(self.__peerToPeerProtocol.send(self, peerToPeerMessage), IPeerToPeerMessage)  
    
    @public
    def route(self, peerToPeerMessage):
        return returns(self.__peerToPeerProtocol.route(self, peerToPeerMessage), IPeerToPeerMessage)
    
    @public
    def getPeerToPeerNetwork(self):
        return returns(self.__peerToPeerNetwork, IPeerToPeerNetwork)
    
    def __eq__(self, other):
        requires(other, IPeer)
        pre_condition(other, lambda x: x <> None)
        return returns(self.__id == other.getId(), bool)
    
    @public
    def addNeighbor(self, neighbor):
        if self.__neighbors.has_key(neighbor.getId()):
            return False
        self.__neighbors[neighbor.getId()] = neighbor
        return returns(self.__neighbors.has_key(neighbor.getId()), bool)
    
    @public
    def removeNeighbor(self, peerId):
        if not self.__neighbors.has_key(peerId):
            return False
        del self.__neighbors[peerId]
        return returns(not self.__neighbors.has_key(peerId), bool)
    
    @public
    def countNeighbors(self):
        return returns(len(self.__neighbors), int)
    
    @public
    def hasNeighbor(self, peerId):
        return returns(self.__neighbors.has_key(peerId), bool)
    
    @public
    def getNeighbor(self, peerId):
        if not self.__neighbors.has_key(peerId):
            return None
        return returns(self.__neighbors[peerId], INeighbor)
    
    @public
    def getPeerToPeerProtocol(self):
        return returns(self.__peerToPeerProtocol, IPeerToPeerProtocol)
    
    @public
    def configure(self, peerToPeerMessageHandlers):
        numHandlers = 0
        for handler in peerToPeerMessageHandlers:
            self.__peerToPeerMessageDispatcher.registerPeerToPeerMessageHandler(handler)
            numHandlers += 1
        return returns(numHandlers, int)
    
    @public
    def getNeighbors(self):
        sem = Semaphore()
        sem.acquire()
        
        values = self.__neighbors.values()
        
        sem.release()
            
        return values
    
    @public
    def getPeerToPeerMessageDispatcher(self):
        return self.__peerToPeerMessageDispatcher
    
    @public
    def getContextManager(self):
        return self.__contextManager
    
    @public
    def getSocialProfile(self):
        return self.__socialProfile
    
    @public
    def push(self, peerToPeerMessage):
        return returns(self.__peerToPeerProtocol.push(self, peerToPeerMessage), IPeerToPeerMessage)
    
    @public
    def setJoinTime(self, time):
        self.__joinTime = time
        return self.__joinTime
    
    @public
    def getJoinTime(self):
        return self.__joinTime
    
    @public
    def shareHardware(self, priority, deviceType, sharedPercentage, opportunityId):
        if not self.isJoined():
            return None
        sem = Semaphore()
        sem.acquire()
        contextManager = self.getContextManager()
        if not contextManager.hasContext(IContext.OPPORTUNITY, opportunityId):
            return None
        
        opportunity = contextManager.getContext(IContext.OPPORTUNITY, opportunityId)
        
        node = self.getNode()
        nodeDevice = node.getNodeDevice(deviceType)
        capacity = nodeDevice.getFreeCapacity() * sharedPercentage
        
        hardwareSharing = None
        if deviceType == INode.DISK:
            hardwareSharing = DiskSharing(HardwareSharingIdGenerator.generateId(self, opportunity, deviceType), self, capacity)
        elif deviceType == INode.MEMORY:
            hardwareSharing = MemorySharing(HardwareSharingIdGenerator.generateId(self, opportunity, deviceType), self, capacity)
        elif deviceType == INode.PROCESSOR:
            hardwareSharing = ProcessorSharing(HardwareSharingIdGenerator.generateId(self, opportunity, deviceType), self, capacity)
        
        sharings = self.__hardwareSharings[deviceType]
        sharings[hardwareSharing.getId()] = hardwareSharing
        
        sem.release()
        
        return hardwareSharing
    
    @public
    def getHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return None
        sharing = self.__hardwareSharings[nodeDeviceType]
        if not sharing.has_key(sharingId):
            return None
        return sharing[sharingId]
    
    @public
    def getSharedCapacity(self, nodeDeviceType):
        capacity = 0
        
        if self.__hardwareSharings.has_key(nodeDeviceType):
            sharings = self.__hardwareSharings[nodeDeviceType]
            for sharing in sharings.values():
                capacity += sharing.getCapacity()
                
        return capacity
    
    @public
    def getFreeSharedCapacity(self, nodeDeviceType):
        capacity = 0
        sem = Semaphore()
        sem.acquire()
        if self.__hardwareSharings.has_key(nodeDeviceType):
            sharings = self.__hardwareSharings[nodeDeviceType]
            if len(sharings) > 0:
                for sharing in sharings.values():
                    capacity += sharing.getFreeCapacity()
            else:
                nodeDevice = self.__node.getNodeDevice(nodeDeviceType)
                capacity = nodeDevice.getCapacity()
        sem.release()           
        return capacity
    
    @public
    def getNodeDeviceCapacity(self, nodeDeviceType):
        sem = Semaphore()
        sem.acquire()
        nodeDevice = self.__node.getNodeDevice(nodeDeviceType)
        sem.release()
        return nodeDevice.getCapacity()
    
    @public
    def getNodedeviceFreeCapacity(self, nodeDeviceType):
        sem = Semaphore()
        sem.acquire()
        nodeDevice = self.__node.getNodeDevice(nodeDeviceType)
        sem.release()
        return nodeDevice.getFreeCapacity()
    
    id = property(getId, None, None, None)

    type = property(getType, None, None, None)

    node = property(getNode, setNode, None, None)

    peerToPeerNetwork = property(getPeerToPeerNetwork, None, None, None)

    peerToPeerProtocol = property(getPeerToPeerProtocol, None, None, None)
    
    contextManager = property(getContextManager, None, None, None)

    socialProfile = property(getSocialProfile, None, None, None)
