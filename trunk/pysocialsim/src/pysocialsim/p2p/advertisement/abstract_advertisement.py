from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractAdvertisement(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, name, peerId, elementId, folksonomies, type):
        self.__name = name
        self.__elementId = elementId
        self.__peerId = peerId
        self.__folksonomies = folksonomies
        self.__type = type
    
    @public
    def getName(self):
        return self.__name
    
    @public
    def getElementId(self):
        return self.__elementId
    
    @public
    def getFolksonomies(self):
        return self.__folksonomies
    
    @public
    def getType(self):
        return self.__type
    
    @public
    def getPeerId(self):
        return self.__peerId