from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

class AbstractInterest(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, folksonomy):
        self.__folksonomy = folksonomy
        self.__reputations = []
    
    @public    
    def getFolksonomy(self):
        return self.__folksonomy
    
    @public
    def addReputation(self, reputation):
        self.__reputations.append(reputation)
    
    @public
    def removeReputation(self, index):
        self.__reputations.remove(index)
    
    @public
    def countReputations(self):
        return len(self.__reputations)
    
    @public
    def getReputations(self):
        return ImmutableSet(self.__reputations)
    
    @public
    def calculateReputationDegree(self, reputationMetric):
        raise NotImplementedError()