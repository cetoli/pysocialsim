from pysocialsim.base.interface import Interface

class ISocialRelationship(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getTargetId(self):
        raise NotImplementedError()
    
    def getSharedDiskSpace(self):
        raise NotImplementedError()
    
    def setSharedDiskSpace(self, sharedDiskSpace):
        raise NotImplementedError()
    
    def addSharedContentId(self, sharedContentId):
        raise NotImplementedError()
    
    def removeSharedContentId(self, sharedContentId):
        raise NotImplementedError()
    
