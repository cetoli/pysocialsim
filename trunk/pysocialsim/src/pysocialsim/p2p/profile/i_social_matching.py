from pysocialsim.base.interface import Interface

class ISocialMatching(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getPeerId(self):
        raise NotImplementedError()
    
    def getElementId(self):
        raise NotImplementedError()
    
    def getPercentage(self):
        raise NotImplementedError()
    
    