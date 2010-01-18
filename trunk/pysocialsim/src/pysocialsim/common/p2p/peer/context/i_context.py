"""
Defines the module with the specification of IContext interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 05/11/2009
"""

class IContext(object):
    
    INTEREST = "INTEREST"
    OPPORTUNITY = "OPPORTUNITY"
    

    def __init__(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def registerTag(self, tag):
        raise NotImplementedError()
    
    def unregisterTag(self, tag):
        raise NotImplementedError()
    
    def countTags(self):
        raise NotImplementedError()
    
    def getTags(self):
        raise NotImplementedError()    