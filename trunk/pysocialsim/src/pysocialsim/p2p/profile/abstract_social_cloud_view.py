from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractSocialCloudView(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id):
        self.__id = id
        self.__socialRelationships = {}
        self.__sharedContents = {}
    
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
        raise NotImplementedError()
    
    @public
    def getSharedContents(self):
        raise NotImplementedError()
    
    @public
    def countSharedContents(self):
        raise NotImplementedError()
    
    @public
    def getSize(self):
        raise NotImplementedError()