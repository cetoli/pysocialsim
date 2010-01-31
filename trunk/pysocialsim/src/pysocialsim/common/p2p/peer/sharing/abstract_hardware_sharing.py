'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.peer.sharing.abstract_sharing import AbstractSharing
from pysocialsim.common.p2p.peer.sharing.i_sharing import ISharing
from pysocialsim.common.p2p.peer.sharing.i_hardware_sharing import IHardwareSharing
from pysocialsim.common.base.decorators import public

class AbstractHardwareSharing(AbstractSharing, IHardwareSharing):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, peer, capacity, nodeDeviceType):
        AbstractSharing.initialize(self, id, peer, ISharing.HARDWARE)
        self.__capacity = capacity
        self.__nodeDeviceType = nodeDeviceType
        
    @public
    def getCapacity(self):
        return self.__capacity
    
    @public
    def getNode(self):
        return self.get_peer().getNode()
    
    @public
    def getNodeDeviceType(self):
        return self.__nodeDeviceType

    @public
    def getFreeCapacity(self):
        return self.__capacity
    
    @public
    def getUsedCapacity(self):
        return 0
    
        
    