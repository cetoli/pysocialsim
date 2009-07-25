from pysocialsim.base.interface import Interface

class IMatchingStrategy(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def execute(self, interest, advertisement):
        raise NotImplementedError()
    
    def setProfile(self, profile):
        raise NotImplementedError()
    
    def getProfile(self):
        raise NotImplementedError()