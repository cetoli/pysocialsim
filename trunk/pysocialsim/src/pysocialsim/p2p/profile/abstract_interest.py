from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

class AbstractInterest(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, type, initialThreshold, limitThreshold, folksonomies):
        self.__type = type
        self.__initialThreshold = initialThreshold
        self.__limitThreshold = limitThreshold
        self.__folksonomies = folksonomies
        self.__socialMatchings = {}
    
    @public    
    def getInitialThreshold(self):
        return self.__initialThreshold
    
    @public
    def getLimitThreshold(self):
        return self.__limitThreshold
    
    @public
    def getType(self):
        return self.__type
    
    @public
    def getFolksonomies(self):
        return ImmutableSet(self.__folksonomies)
    
    @public
    def addSocialMatching(self, socialMatching):
        if not self.__socialMatchings.has_key(socialMatching.getPeerId()):
            self.__socialMatchings[socialMatching.getPeerId()] = {}
        matchings = self.__socialMatchings[socialMatching.getPeerId()]
        if not matchings.has_key(socialMatching.getElementId()):
            matchings[socialMatching.getElementId()] = socialMatching
    
    @public        
    def removeSocialMatching(self, socialMatching):
        if self.__socialMatchings.has_key(socialMatching.getPeerId()):
            matchings = self.__socialMatchings[socialMatching.getPeerId()]
            if matchings.has_key(socialMatching.getElementId()):
                del matchings[socialMatching.getElementId()]
                if len(matchings) == 0:
                    del self.__socialMatchings[socialMatching.getPeerId()]
    @public
    def getMatchedPeers(self):
        return self.__socialMatchings.keys()
    
    @public
    def getSocialMatchings(self, peer):
        return self.__socialMatchings[peer]
    
    @public
    def countMatchedPeers(self):
        return len(self.__socialMatchings)
    
    @public
    def countSocialMatchings(self, peer):
        return len(self.__socialMatchings[peer])
        