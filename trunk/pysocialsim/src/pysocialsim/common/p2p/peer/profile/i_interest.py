"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/01/2010
"""

class IInterest(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getConcept(self):
        raise NotImplementedError()
    
    def registerTag(self, tag):
        raise NotImplementedError()
    
    def unregisterTag(self, tag):
        raise NotImplementedError()
    
    def getTags(self):
        raise NotImplementedError()
    
    def getSocialProfile(self):
        raise NotImplementedError()
    
    def setSocialProfile(self, socialProfile):
        raise NotImplementedError()
    
    def countTags(self):
        raise NotImplementedError()
    
    def hasTag(self, tag):
        raise NotImplementedError()
    
    def getTagAccount(self, tag):
        raise NotImplementedError()
    
    def matchInterest(self, interest):
        raise NotImplementedError()
    