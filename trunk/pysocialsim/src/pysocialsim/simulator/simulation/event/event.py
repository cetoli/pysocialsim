from pysocialsim.base.interface import Interface

class Event(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def getPriority(self):
        raise NotImplementedError()
    
    def handled(self):
        raise NotImplementedError()
    
    def isHandled(self):
        raise NotImplementedError()