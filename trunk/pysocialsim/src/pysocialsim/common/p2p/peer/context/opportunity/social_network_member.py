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
        self.__active = True
    
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
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if sharings.has_key(hardwareSharingContext.getId()):
            return False
        print "INSERIU AQUI ESSA PORRA"
        
        sharings[hardwareSharingContext.getId()] = hardwareSharingContext
        return sharings.has_key(hardwareSharingContext.getId())
    
    @public
    def hasHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return False
        
        return self.__hardwareSharings.has_key(sharingId)
    
    @public
    def unregisterHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return False
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return False
        del sharings[sharingId]
        return not sharings.has_key(sharingId)
    
    @public
    def getHardwareSharing(self, nodeDeviceType, sharingId):
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return None
        sharings = self.__hardwareSharings[nodeDeviceType]
        if not sharings.has_key(sharingId):
            return None
        return sharings[sharingId]
    
    @public
    def getHardwareSharings(self, nodeDeviceType):
        if not self.__hardwareSharings.has_key(nodeDeviceType):
            return None
        
        sharings = self.__hardwareSharings[nodeDeviceType]
        return sharings.values()
    
    @public
    def clone(self):
        cln = SocialNetworkMember(self.__id)
        disks = self.__hardwareSharings[INode.DISK]
        for disk in disks.values():
            cln.registerHardwareSharing(INode.DISK, disk.clone())
        
        memories = self.__hardwareSharings[INode.MEMORY]
        for memory in memories.values():
            cln.registerHardwareSharing(INode.MEMORY, memory.clone())
            
        processors = self.__hardwareSharings[INode.PROCESSOR]
        for processor in processors.values():
            cln.registerHardwareSharing(INode.PROCESSOR, processor.clone())
            
        return cln
    
    @public
    def activate(self):
        self.__active = True
        
    @public
    def deactive(self):
        self.__active = False
        
    @public
    def isActive(self):
        return self.__active == True