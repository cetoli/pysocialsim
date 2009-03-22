from pysocialsim.base.interface import Interface

class MessageSubject(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def notifyMessageObservers(self, message):
        raise NotImplementedError()
    
    def addMessageObserver(self, observer):
        raise NotImplementedError()
    
    def removeMessageObserver(self, messageName):
        raise NotImplementedError()
    
    def countMessageObservers(self, messageName):
        raise NotImplementedError()