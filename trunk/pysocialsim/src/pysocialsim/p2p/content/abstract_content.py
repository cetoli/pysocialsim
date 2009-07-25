from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from sets import ImmutableSet

class AbstractContent(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, folksonomies, size):
        self.__id = id
        self.__folksonomies = folksonomies
        self.__owners = []
        self.__size = size
    
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