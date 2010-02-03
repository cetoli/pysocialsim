'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.peer.sharing.i_sharing import ISharing

class IHardwareSharing(ISharing):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getNodeDeviceType(self):
        raise NotImplementedError()
    
    def getCapacity(self):
        raise NotImplementedError()
    
    def getFreeCapacity(self):
        raise NotImplementedError()
    
    def getUsedCapacity(self):
        raise NotImplementedError()
    
    def getNode(self):
        raise NotImplementedError()
    
    def clone(self):
        raise NotImplementedError()