from pysocialsim.base.interface import Interface

class Necessity(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    def setAttribute(self, name, value):
        raise NotImplementedError()
    
    def getAttribute(self, name):
        raise NotImplementedError()
    
    def removeAttribute(self, name):
        raise NotImplementedError()
    
    def countAttributes(self):
        raise NotImplementedError()
    
    def getAttributes(self):
        raise NotImplementedError()
    
    def getMinimumTrustDegree(self):
        raise NotImplementedError()
    
    def getMaximumTrustDegree(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def getMaximumMatchingNumber(self):
        raise NotImplementedError()