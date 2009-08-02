from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractSocialMatching(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, peerId, elementId, percentage):
        self.__peerId = peerId
        self.__elementId = elementId
        self.__percentage = percentage
    
    @public    
    def getPeerId(self):
        return self.__peerId
    
    @public
    def getElementId(self):
        return self.__elementId
    
    @public
    def getPercentage(self):
        return self.__percentage
    
    