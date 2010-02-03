'''
Created on 31/01/2010

@author: fabricio
'''

class IHardwareSharingContextInformation(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getCapacity(self):
        raise NotImplementedError()
    
    def getUsedCapacity(self):
        raise NotImplementedError()
    
    def getFreeCapacity(self):
        raise NotImplementedError()
    
    def getPeerId(self):
        raise NotImplementedError()
    
    def getNodeDeviceType(self):
        raise NotImplementedError()

    def clone(self):
        raise NotImplementedError()