from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractInterestMatchingStrategy(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__profile = None
    
    @public    
    def setProfile(self, profile):
        self.__profile = profile
    
    @public
    def getProfile(self):
        return self.__profile