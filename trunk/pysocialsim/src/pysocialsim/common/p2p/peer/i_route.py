"""
Defines the module with the specification of IRoute interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/10/2009
"""

class IRoute(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getPeerId(self):
        raise NotImplementedError()
    
    def getTrace(self):
        raise NotImplementedError()
    
    def setTrace(self, trace):
        raise NotImplementedError()
    
    def getHops(self):
        raise NotImplementedError()
    
    def getCost(self):
        raise NotImplementedError()
    
    def setCost(self, cost):
        raise NotImplementedError()
    
    def registerTag(self, tag):
        raise NotImplementedError()
    
    def unregisterTag(self, tag):
        raise NotImplementedError()
    
    def countTags(self):
        raise NotImplementedError()
    
    def getTags(self):
        raise NotImplementedError()
    
    def getTagIncidence(self, tag):
        raise NotImplementedError()
    
    def setFreshness(self, freshness):
        raise NotImplementedError()
    
    def getFreshness(self):
        raise NotImplementedError()