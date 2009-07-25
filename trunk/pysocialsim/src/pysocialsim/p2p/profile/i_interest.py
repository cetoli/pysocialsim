from pysocialsim.base.interface import Interface

class IInterest:
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getInitialThreshold(self):
        raise NotImplementedError()
    
    def getLimitThreshold(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    def getFolksonomies(self):
        raise NotImplementedError()