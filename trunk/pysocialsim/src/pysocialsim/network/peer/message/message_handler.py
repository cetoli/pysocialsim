from pysocialsim.base.interface import Interface

class MessageHandler(object):
    
    __interface__ = Interface
    
    def getMessageName(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def clone(self):
        raise NotImplementedError()
    
    def getMessage(self):
        raise NotImplementedError()
    
    def handleMessage(self, message):
        raise NotImplementedError()