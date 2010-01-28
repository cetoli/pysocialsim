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