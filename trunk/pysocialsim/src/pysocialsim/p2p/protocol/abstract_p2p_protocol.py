from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
from types import NoneType
from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler
from sets import ImmutableSet
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage

class AbstractP2PProtocol(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__peer = None
        self.__topology = None
        self.__messageHandlers = {}
    
    def registerMessageHandler(self, messageHandler):
        self.__messageHandlers[messageHandler.getMessageName()] = messageHandler
    
    def unregisterMessageHandler(self, messageName):
        pass
    
    @public    
    def sendMessage(self, message):
        raise NotImplementedError()
    
    @public
    def receiveMessage(self, message):
        raise NotImplementedError()
    
    @public
    def advertise(self, element, advertisementType):
        raise NotImplementedError()
    
    @public
    def setPeer(self, peer):
        self.__peer = peer
        return self.__peer
    
    @public
    def getPeer(self):
        return self.__peer
    
    @public
    def connect(self, priority):
        raise NotImplementedError()
    
    @public
    def disconnect(self, priority):
        raise NotImplementedError()
    
    @public
    def clone(self):
        raise NotImplementedError()
    
    @public
    def setP2PTopology(self, topology):
        self.__topology = topology
        return self.__topology
    
    @public
    def getP2PTopology(self):
        return self.__topology
    
    @public
    def getMessageHandlers(self):
        return ImmutableSet(self.__messageHandlers.values())