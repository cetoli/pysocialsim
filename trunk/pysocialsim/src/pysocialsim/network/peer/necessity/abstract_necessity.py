from pysocialsim.base.object import Object
from sets import ImmutableSet
from pysocialsim.base.decorator.public import public

class AbstractNecessity(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, type, peer, minimumTrustDegree, maximumTrustDegree, maximumMatchingNumber):
        self.__type = type
        self.__peer = peer
        self.__attributes = {}
        self.__minimumTrustDegree = minimumTrustDegree
        self.__maximumTrustDegree = maximumTrustDegree
        self.__maximumMatchingNumber = maximumMatchingNumber
        
    @public
    def getType(self):
        return self.__type
    
    @public
    def setAttribute(self, name, value):
        self.__attributes[name] = value
    
    @public
    def getAttribute(self, name):
        return self.__attributes[name]
    
    @public
    def removeAttribute(self, name):
        del self.__attributes[name]
    
    @public
    def countAttributes(self):
        return len(self.__attributes)
    
    @public
    def getAttributes(self):
        return ImmutableSet(self.__attributes.values())
    
    @public
    def getMinimumTrustDegree(self):
        return self.__minimumTrustDegree
    
    @public
    def getMaximumTrustDegree(self):
        return self.__maximumTrustDegree
    
    @public
    def getMaximumMatchingNumber(self):
        return self.__maximumMatchingNumber