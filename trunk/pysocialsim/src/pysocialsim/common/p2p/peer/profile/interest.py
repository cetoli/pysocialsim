"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/01/2010
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.profile.i_interest import IInterest
from pysocialsim.common.base.decorators import public

class Interest(Object, IInterest):
    
    def __init__(self, concept):
        self.initialize(concept)

    def initialize(self, concept):
        self.__concept = concept
        self.__tags = {}
        self.__socialProfile = None
        
    @public
    def getConcept(self):
        return self.__concept

    @public
    def getTags(self):
        return self.__tags.keys()

    @public
    def getSocialProfile(self):
        return self.__socialProfile

    @public
    def setSocialProfile(self, socialProfile):
        self.__socialProfile = socialProfile
    
    @public    
    def registerTag(self, tag):
        if not self.__tags.has_key(tag):
            self.__tags[tag] = 1
        self.__tags[tag] += 1
        return self.__tags[tag]
    
    @public
    def unregisterTag(self, tag):
        if not self.__tags.has_key(tag):
            return 0
        else:
            self.__tags[tag] -= 1
            if self.__tags[tag] == 0:
                del self.__tags[tag]
                return 0
            return self.__tags[tag]
    
    @public
    def countTags(self):
        return len(self.__tags)
    
    @public
    def hasTag(self, tag):
        return self.__tags.has_key(tag)
    
    @public
    def getTagAccount(self, tag):
        if not self.__tags[tag]:
            return 0
        return self.__tags[tag]
    
    @public
    def matchInterest(self, interest):
        return 0

    
    concept = property(getConcept, None, None, None)

    tags = property(getTags, None, None, None)

    socialProfile = property(getSocialProfile, setSocialProfile, None, None)
