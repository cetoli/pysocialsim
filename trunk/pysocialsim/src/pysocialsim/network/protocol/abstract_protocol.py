from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

class AbstractProtocol(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__peer = None
        self.__messageHandlers = {}
        self.__topology = None
    
    @public    
    def sendMessage(self, message):
        raise NotImplementedError()
    
    @public
    def receiveMessage(self, message):
        raise NotImplementedError()
    
    @public
    def advertise(self, advertisementType):
        raise NotImplementedError()
    
    @public
    def setPeer(self, peer):
        self.__peer = peer
        return self.__peer
    
    @public
    def getPeer(self):
        return self.__peer
    
    @public
    def registerMessageHandlerClass(self, messageName, messageHandlerClass):
        self.__messageHandlers[messageName] = messageHandlerClass
    
    @public
    def unregisterMessageHandlerClass(self, messageName):
        del self.__messageHandlers[messageName]
    
    @public
    def countMessageHandlers(self):
        return len(self.__messageHandlers)
    
    @public
    def clone(self):
        raise NotImplementedError()
    
    @public
    def setTopology(self, topology):
        self.__topology = topology
        return self.__topology
    
    @public
    def getTopology(self):
        return self.__topology
    
    @public
    def getMessageHandlerClasses(self):
        return ImmutableSet(self.__messageHandlers.values())
    
    @public
    def connect(self):
        raise NotImplementedError()
    
    @public
    def disconnect(self):
        raise NotImplementedError()