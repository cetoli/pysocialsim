'''
Created on 31/01/2010

@author: fabricio
'''

class ISharing(object):
    
    HARDWARE = "HARDWARE"
    CONTENT = "CONTENT"
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def getContext(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def getType(self):
        raise NotImplementedError()
    
    
