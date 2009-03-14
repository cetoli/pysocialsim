from pysocialsim.base.interface import Interface

class MessageDispatcher(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def handleMessage(self, message):
        raise NotImplementedError()
    
    def registerMessageHandler(self, handler):
        raise NotImplementedError()
    
    def unregisterMessageHandler(self, handle):
        raise NotImplementedError()
    
    def countMessageHandlers(self):
        raise NotImplementedError()