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
        pass
    