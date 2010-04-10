"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 19/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public

class InterestConstraint(Object):
    
    def __init__(self, threshold, interest):
        self.initialize(threshold, interest)
    
    def initialize(self, threshold, interest):
        self.__threshold = threshold
        self.__interest = interest
        
    @public
    def getInterest(self):
        return self.__interest
    
    @public
    def getConcept(self):
        return self.__interest.getConcept()
    
    @public
    def getThreshold(self):
        return self.__threshold
    
    @public
    def satisfyInterest(self, socialProfile):
        return socialProfile.matchInterest(self.__interest) >= self.__threshold