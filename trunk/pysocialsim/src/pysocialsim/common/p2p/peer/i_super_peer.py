"""
Defines the module with the specification ISuperPeer interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/10/2009
"""

class ISuperPeer(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def countChildren(self):
        raise NotImplementedError();
        