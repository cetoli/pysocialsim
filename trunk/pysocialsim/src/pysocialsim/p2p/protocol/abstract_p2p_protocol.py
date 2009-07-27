from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

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