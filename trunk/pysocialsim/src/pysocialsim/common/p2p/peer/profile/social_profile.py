"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.profile.i_social_profile import ISocialProfile
from pysocialsim.common.base.decorators import public

class SocialProfile(Object, ISocialProfile):
    
    def __init__(self, peer):
        self.initialize(peer)

    def initialize(self, peer):
        self.__peer = peer
        self.__interests = {}
    
    @public    
    def getId(self):
        return self.__peer.getId()

    @public
    def addInterest(self, interest):
        if self.__interests.has_key(interest.getConcept()):
            return False
        self.__interests[interest.getConcept()] = interest
        interest.setSocialProfile(self)
        return True

    @public
    def removeInterest(self, concept):
        if not self.__interests.has_key(concept):
            return False
        del self.__interests[concept]
        return True

    @public
    def getInterest(self, concept):
        if not self.__interests.has_key(concept):
            return False
        return self.__interests[concept]

    @public
    def getInterests(self):
        return self.__interests.values()

    @public
    def countInterests(self):
        return len(self.__interests)

    @public
    def hasInterest(self, concept):
        return self.__interests.has_key(concept)

    @public
    def matchInterest(self, interest):
        if not self.__interests.has_key(interest.getConcept()):
            return 0.0
        return self.__interests[interest.getConcept()].matchInterest(interest)
        
    