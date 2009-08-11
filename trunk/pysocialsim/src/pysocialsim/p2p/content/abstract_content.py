from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet

class AbstractContent(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, folksonomies, size):
        self.__id = id
        self.__folksonomies = folksonomies
        self.__owners = []
        self.__size = size
        self.__socialClouds = []
    
    @public
    def getId(self):
        return self.__id
    
    @public
    def addFolksonomy(self, folksonomy):
        self.__folksonomies.append(folksonomy)
        return self.__folksonomies[self.__folksonomies.index(folksonomy)]
    
    @public
    def removeFolksonomy(self, folksonomy):
        tag = self.__folksonomies[self.__folksonomies.index(folksonomy)]
        self.__folksonomies.remove(folksonomy)
        return tag
    
    @public
    def countFolksonomies(self):
        return len(self.__folksonomies)
    
    @public
    def getFolksonomies(self):
        return ImmutableSet(self.__folksonomies)
    
    @public
    def addOwner(self, peerId):
        self.__owners.append(peerId)
        return self.__owners[self.__owners.index(peerId)]
    
    @public
    def removeOwner(self, peerId):
        owner = self.__owners[self.__owners.index(peerId)]
        self.__owners.remove(peerId)
        return owner
    
    @public
    def countOwners(self):
        return len(self.__owners)
    
    @public
    def getOwners(self):
        return ImmutableSet(self.__owners)
    
    @public
    def hasFolksonomy(self, folksonomy):
        return folksonomy in self.__folksonomies
    
    @public
    def getSize(self):
        return self.__size
    
    @public
    def clone(self):
        raise NotImplementedError()
    
    @public
    def addSocialCloud(self, cloudId):
        self.__socialClouds.append(cloudId)
    
    @public
    def removeSocialCloud(self, cloudId):
        self.__socialClouds.remove(cloudId)
    
    @public
    def countSocialClouds(self):
        return len(self.__socialClouds)
    
    @public
    def hasSocialCloud(self, cloudId):
        return cloudId in self.__socialClouds