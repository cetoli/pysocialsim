from pysocialsim.base.object import Object

class AbstractSocialCloudView(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id):
        self.__id = id
        self.__socialRelationships = {}
        self.__sharedContents = {}
    
    def getId(self):
        return self.__id
    
    def addSocialRelationship(self, relationship):
        self.__socialRelationships[relationship.getTargetId()] = relationship
    
    def removeSocialRelationship(self, relationship):
        del self.__socialRelationships[relationship.getTargetId()]
    
    def getRelationships(self):
        return self.__socialRelationships.values()
    
    def countRelationships(self):
        return len(self.__socialRelationships)
    
    def addSharedContent(self, sharedContent):
        raise NotImplementedError()
    
    def removeSharedContent(self, sharedContent):
        raise NotImplementedError()
    
    def getSharedContents(self):
        raise NotImplementedError()
    
    def countSharedContents(self):
        raise NotImplementedError()
    
    def getSize(self):
        raise NotImplementedError()