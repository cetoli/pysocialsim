
class ISocialCloudView(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def addSocialRelationship(self, relationship):
        raise NotImplementedError()
    
    def removeSocialRelationship(self, relationship):
        raise NotImplementedError()
    
    def getRelationships(self):
        raise NotImplementedError()
    
    def countRelationships(self):
        raise NotImplementedError()
    
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