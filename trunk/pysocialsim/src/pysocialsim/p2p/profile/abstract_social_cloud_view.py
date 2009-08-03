from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractSocialCloudView(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, sharedDiskSpace):
        self.__id = id
        self.__socialRelationships = {}
        self.__sharedContents = {}
        self.__sharedDiskSpace = sharedDiskSpace
    
    @public
    def getId(self):
        return self.__id
    
    @public
    def addSocialRelationship(self, relationship):
        self.__socialRelationships[relationship.getTargetId()] = relationship
    
    @public
    def removeSocialRelationship(self, relationship):
        del self.__socialRelationships[relationship.getTargetId()]
    
    @public
    def getRelationships(self):
        return self.__socialRelationships.values()
    
    @public
    def countRelationships(self):
        return len(self.__socialRelationships)
    
    @public
    def addSharedContent(self, sharedContent):
        self.__sharedContents[sharedContent.getId()] = sharedContent
    
    @public
    def removeSharedContent(self, sharedContent):
        del self.__sharedContents[sharedContent.getId()]
    
    @public
    def getSharedContents(self):
        return self.__sharedContents.values()
    
    @public
    def countSharedContents(self):
        return len(self.__sharedContents)
    
    @public
    def getSize(self):
        raise NotImplementedError()
    
    @public
    def getRelationship(self, peerId):
        return self.__socialRelationships[peerId]
    
    @public
    def getSharedDiskSpace(self):
        return self.__sharedDiskSpace
    
    @public
    def setSharedDiskSpace(self, sharedDiskSpace):
        self.__sharedDiskSpace = sharedDiskSpace