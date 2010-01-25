"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/01/2010
"""

class ISocialProfile(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def addInterest(self, interest):
        raise NotImplementedError()
    
    def removeInterest(self, concept):
        raise NotImplementedError()
    
    def getInterest(self, concept):
        raise NotImplementedError()
    
    def getInterests(self):
        raise NotImplementedError()
    
    def countInterests(self):
        raise NotImplementedError()
    
    def hasInterest(self, concept):
        raise NotImplementedError()
    
    def matchInterest(self, interest):
        raise NotImplementedError()