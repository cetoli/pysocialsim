from pysocialsim.base.interface import Interface

class IAdvertisement:
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        raise NotImplementedError()
    
    def getElementId(self):
        raise NotImplementedError()
    
    def getFolksonomies(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    def getPeerId(self):
        raise NotImplementedError()