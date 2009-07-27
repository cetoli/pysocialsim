from pysocialsim.base.object import Object

class AbstractSocialRelationship(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, targetId, sharedDiskSpace):
        self.__targetId = targetId
        self.__sharedDiskSpace = sharedDiskSpace
        
    def getTargetId(self):
        return self.__targetId
    
    def getSharedDiskSpace(self):
        return self.__sharedDiskSpace
    
    def setSharedDiskSpace(self, sharedDiskSpace):
        self.__sharedDiskSpace = sharedDiskSpace