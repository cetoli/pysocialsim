'''
Created on 02/02/2010

@author: fabricio
'''

class IContent(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def getSize(self):
        raise NotImplementedError()
    
    def registerOwner(self, peerId):
        raise NotImplementedError()
    
    def unregisterOwner(self, peerId):
        raise NotImplementedError()
    
    def countOwners(self):
        raise NotImplementedError()
    
    def getOwners(self):
        raise NotImplementedError()