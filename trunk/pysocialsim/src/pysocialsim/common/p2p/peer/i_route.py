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