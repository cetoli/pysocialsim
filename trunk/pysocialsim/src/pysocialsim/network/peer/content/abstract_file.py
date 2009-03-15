from pysocialsim.base.object import Object
from sets import ImmutableSet
from pysocialsim.base.decorator.public import public

class AbstractFile(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, concept, folksonomies):
        self.__id = id
        self.__concept = concept
        self.__folksonomies = folksonomies
        self.__owners = []
    
    @public    
    def getId(self):
        return self.__id
    
    @public
    def addFolksonomy(self, folksonomy):
        self.__folksonomies.append(folksonomy)
        return self.__folksonomies[self.__folksonomies.index(folksonomy)]
    
    @public
    def removeFolksonomy(self, folksonomy):
        return self.__folksonomies.pop(self.__folksonomies.index(folksonomy))
    
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
        return self.__owners.pop(self.__owners.index(peerId))
    
    @public
    def countOwners(self):
        return len(self.__owners)
    
    @public
    def getOwners(self):
        return ImmutableSet(self.__owners)
    
    @public
    def getConcept(self):
        return self.__concept