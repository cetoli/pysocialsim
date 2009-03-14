from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractMessageHandler(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, messageName, peer):
        self.__messageName = messageName
        self.__peer = peer
        self.__message = None
        self.__isHandled = False
        
    @public
    def getMessageName(self):
        return self.__messageName
    
    @public
    def getPeer(self):
        return self.__peer
    
    @public
    def clone(self):
        raise NotImplementedError()
    
    @public
    def getMessage(self):
        return self.__message
    
    @public
    def handleMessage(self, message):
        self.__message = message
        self.executeHandler(message)
        
    def executeHandler(self, message):
        raise NotImplementedError()
    
    @public
    def handled(self):
        self.__isHandled = True
        return self.__isHandled
        
    @public
    def isHandled(self):
        return self.__isHandled