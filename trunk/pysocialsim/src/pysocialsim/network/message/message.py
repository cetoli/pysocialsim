from pysocialsim.base.interface import Interface

class Message(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getSourceId(self):
        raise NotImplementedError()
    
    def getTargetId(self):
        raise NotImplementedError()
    
    def getTTL(self):
        raise NotImplementedError()
    
    def registerTrace(self, id):
        raise NotImplementedError()
    
    def unregisterTrace(self):
        raise NotImplementedError()
    
    def countTraces(self):
        raise NotImplementedError()
    
    def getTrace(self, index):
        raise NotImplementedError()
    
    def getTraces(self):
        raise NotImplementedError()
    
    def getFirstTrace(self):
        raise NotImplementedError()
    
    def getLastTrace(self):
        raise NotImplementedError()
    
    def getName(self):
        raise NotImplementedError()