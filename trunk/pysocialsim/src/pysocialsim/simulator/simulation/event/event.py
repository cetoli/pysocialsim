from pysocialsim.base.interface import Interface

class Event(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        raise NotImplementedError()
    
    def getPeer(self, peer):
        raise NotImplementedError()