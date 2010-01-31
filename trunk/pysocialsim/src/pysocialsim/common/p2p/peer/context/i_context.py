"""
Defines the module with the specification of IContext interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 05/11/2009
"""

class IContext(object):
    
    OPPORTUNITY = "OPPORTUNITY"
    HARDWARE_SHARING = "HARDWARE_SHARING"
    CONTENT_SHARING = "CONTENT_SHARING"
    
    

    def __init__(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def getVersion(self):
        raise NotImplementedError()
    
    def setVersion(self, version):
        raise NotImplementedError()