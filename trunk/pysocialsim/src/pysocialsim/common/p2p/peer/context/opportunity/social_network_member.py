"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.topology.graph.i_node import INode

class SocialNetworkMember(Object):
    
    def __init__(self, id):
        self.initialize(id)
    
    def initialize(self, id):
        self.__id = id
        self.__socialNetwork = None
        self.__hardwareSharings = {INode.DISK: {}, INode.MEMORY: {}, INode.PROCESSOR: {}}
    
    @public    
    def getId(self):
        return self.__id
    
    @public
    def getSocialNetwork(self):
        return self.__socialNetwork
    
    @public
    def setSocialNetwork(self, socialNetwork):
        self.__socialNetwork = socialNetwork
        return self.__socialNetwork
    
    @public
    def registerHardwareSharing(self, nodeDeviceType, hardwareSharingContext):
        if not self.__hardwareSharings[nodeDeviceType]:
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(hardwareSharingContext.getId()):
            return False
        sharings[hardwareSharingContext.getId()] = hardwareSharingContext
        return sharings.has_key(hardwareSharingContext.getId())
    
    @public
    def hasHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings[nodeDeviceType]:
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return False
        return self.__hardwareSharings.has_key(sharingId)
    
    @public
    def unregisterHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings[nodeDeviceType]:
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return False
        del sharings[sharingId]
        return not sharings.has_key(sharingId)
    
    @public
    def getHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings[nodeDeviceType]:
            return None
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return None
        return sharings[sharingId]