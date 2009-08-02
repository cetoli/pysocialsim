from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractSocialRelationship(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, targetId, sharedDiskSpace):
        self.__targetId = targetId
        self.__sharedDiskSpace = sharedDiskSpace
    
    @public    
    def getTargetId(self):
        return self.__targetId
    
    @public
    def getSharedDiskSpace(self):
        return self.__sharedDiskSpace
    
    @public
    def setSharedDiskSpace(self, sharedDiskSpace):
        self.__sharedDiskSpace = sharedDiskSpace