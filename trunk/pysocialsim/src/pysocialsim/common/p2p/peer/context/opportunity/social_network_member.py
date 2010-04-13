"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public

class SocialNetworkMember(Object):
    
    def __init__(self, id):
        self.initialize(id)
    
    def initialize(self, id):
        self.__id = id
        self.__socialNetwork = None
        self.__hardwareSharings = {}
    
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
    def registerHardwareSharing(self, hardwareSharingContext):
        if self.__hardwareSharings.has_key(hardwareSharingContext.getId()):
            return False
        self.__hardwareSharings[hardwareSharingContext.getId()] = hardwareSharingContext
        return self.__hardwareSharings.has_key(hardwareSharingContext.getId())
    
    @public
    def hasHardwareSharing(self, sharingId):
        return self.__hardwareSharings.has_key(sharingId)
    
    @public
    def unregisterHardwareSharing(self, sharingId):
        if not self.__hardwareSharings.has_key(sharingId): 
            return False
        del self.__hardwareSharings[sharingId]
        return not self.__hardwareSharings.has_key(sharingId)
    
    @public
    def getHardwareSharing(self, sharingId):
        if not self.__hardwareSharings.has_key(sharingId):
            return None
        return self.__hardwareSharings[sharingId]
    
    @public
    def getHardwareSharings(self, nodeDeviceType):
        sharings = []
        for sharing in self.__hardwareSharings.values():
            if not sharing.getNodeDeviceType() == nodeDeviceType:
                continue
            sharings.append(sharing)
        return sharings
    
    @public
    def countHardwareSharings(self):
        return len(self.__hardwareSharings)
    
    @public
    def clone(self):
        cln = SocialNetworkMember(self.__id)
        for sharing in self.__hardwareSharings.values():
            cln.registerHardwareSharing(sharing)
            
        return cln