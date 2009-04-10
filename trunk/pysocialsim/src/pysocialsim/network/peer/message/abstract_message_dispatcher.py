from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from threading import Thread

class AbstractMessageDispatcher(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, peer):
        self.__peer = peer
        self.__handlers = {}
        self.__peer.setMessageDispatcher(self)
        
    @public
    def handleMessage(self, message):
        if not self.__handlers.has_key(message.getName()):
            return False
        clone = self.__handlers[message.getName()].clone()
        AbstractMessageDispatcher.MessageHandlingThread(clone, message).start()
        return message
    
    @public
    def registerMessageHandler(self, handler):
        if self.__handlers.has_key(handler.getMessageName()):
            return False
        self.__handlers[handler.getMessageName()] = handler
        return True
    
    @public
    def unregisterMessageHandler(self, handle):
        if not self.__handlers.has_key(handle):
            return False
        del self.__handlers[handle]
        return True
    
    @public
    def countMessageHandlers(self):
        return len(self.__handlers)
    
    class MessageHandlingThread(Thread):
        
        def __init__(self, handler, message):
            Thread.__init__(self)
            self.__handler = handler
            self.__message = message
            
        def run(self):
            self.__handler.handleMessage(self.__message)