from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractSocialRelationship(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, targetId, sharedDiskSpace, targetCloudId):
        self.__targetId = targetId
        self.__targetCloudId = targetCloudId
    
    @public    
    def getTargetId(self):
        return self.__targetId
    
    @public
    def getTargetCloudId(self):
        return self.__targetCloudId
