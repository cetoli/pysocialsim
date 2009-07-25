from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

class AbstractInterest(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, type, initialThreshold, limitThreshold, folksonomies):
        self.__type = type
        self.__initialThreshold = initialThreshold
        self.__limitThreshold = limitThreshold
        self.__folksonomies = folksonomies
    
    @public    
    def getInitialThreshold(self):
        return self.__initialThreshold
    
    @public
    def getLimitThreshold(self):
        return self.__limitThreshold
    
    @public
    def getType(self):
        return self.__type
    
    @public
    def getFolksonomies(self):
        return ImmutableSet(self.__folksonomies)