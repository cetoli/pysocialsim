'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.peer.context.abstract_context import AbstractContext
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.context.sharing.i_hardware_sharing_context_information import IHardwareSharingContextInformation
from pysocialsim.common.base.decorators import public

class AbstractHardwareSharingContextInformation(AbstractContext, IHardwareSharingContextInformation):
    
    def __init__(self):
        raise NotImplementedError()
        
    def initialize(self, id, nodeDeviceType, capacity, usedCapacity, freeCapacity, peerId):
        AbstractContext.initialize(self, IContext.HARDWARE_SHARING, id)
        self.__capacity = capacity
        self.__usedCapacity = usedCapacity
        self.__freeCapacity = freeCapacity
        self.__peerId = peerId
        self.__nodeDeviceType = nodeDeviceType
    
    @public    
    def getCapacity(self):
        return self.__capacity
    
    @public
    def getUsedCapacity(self):
        return self.__usedCapacity
    
    @public
    def getFreeCapacity(self):
        return self.__freeCapacity
    
    @public
    def getPeerId(self):
        return self.__peerId
    
    @public
    def getNodeDeviceType(self):
        return self.__nodeDeviceType
    
