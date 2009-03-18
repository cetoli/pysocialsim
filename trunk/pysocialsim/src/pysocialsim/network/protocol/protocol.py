from pysocialsim.base.interface import Interface

class Protocol(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def sendMessage(self, message):
        raise NotImplementedError()
    
    def receiveMessage(self, message):
        raise NotImplementedError()
    
    def advertise(self, advertisementType):
        raise NotImplementedError()
    
    def setPeer(self, peer):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def registerMessageHandlerClass(self, messageName, handlerClass):
        raise NotImplementedError()
    
    def unregisterMessageHandlerClass(self, messageName):
        raise NotImplementedError()
    
    def countMessageHandlerClasses(self):
        raise NotImplementedError()
    
    def connect(self):
        raise NotImplementedError()
    
    def disconnect(self):
        raise NotImplementedError()
    
    def clone(self):
        raise NotImplementedError()
    
    def setTopology(self, topology):
        raise NotImplementedError()
    
    def getTopology(self):
        raise NotImplementedError()
    
    def getMessageHandlerClasses(self):
        raise NotImplementedError()