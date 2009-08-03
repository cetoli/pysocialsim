from pysocialsim.base.interface import Interface

class ISocialRelationship(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getTargetId(self):
        raise NotImplementedError()
    
    def getTargetCloudId(self):
        raise NotImplementedError()
