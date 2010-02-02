"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public

class SocialNetwork(Object):
    
    def __init__(self, opportunity):
        self.initialize(opportunity)
    
    def initialize(self, opportunity):
        self.__opportunity = opportunity
        self.__members = {}
        
    @public
    def hasSocialNetworkMember(self, peerId):
        return self.__members.has_key(peerId)
    
    @public
    def addSocialNetworkMember(self, member):
        if self.__members.has_key(member.getId()):
            return False
        self.__members[member.getId()] = member
        return self.__members
    
    @public
    def countSocialNetworkMembers(self):
        return len(self.__members)
    
    @public
    def getSocialNetworkMembers(self):
        return self.__members.values()
    
    @public
    def getSocialNetworkMember(self, peerId):
        if not self.__members.has_key(peerId):
            return None
        return self.__members[peerId]
    
    @public
    def getCapacity(self, nodeDeviceType):
        capacity = 0
        for member in self.__members.values():
            for sharing in member.getHardwareSharings(nodeDeviceType):
                capacity += sharing.getCapacity()
                
        return capacity
    
    @public
    def getFreeCapacity(self, nodeDeviceType):
        capacity = 0
        for member in self.__members.values():
            for sharing in member.getHardwareSharings(nodeDeviceType):
                capacity += sharing.getFreeCapacity()
        if capacity == 0:
            capacity = self.getCapacity(nodeDeviceType)
        return capacity
    
    @public
    def getUsedCapacity(self, nodeDeviceType):
        return self.getCapacity(nodeDeviceType) - self.getFreeCapacity(nodeDeviceType)
    
    @public
    def clone(self):
        cln = SocialNetwork(self.__opportunity)
        for member in self.__members.values():
            self.__members[member.getId()] = member.clone()
        return cln
    