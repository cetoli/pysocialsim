from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require

class AbstractMessage(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @require("name", str)
    @require("sourceId", int)
    @require("targetId", int)
    @require("ttl", int)
    def initialize(self, name, sourceId, targetId, ttl):
        self.__name = name
        self.__sourceId = sourceId
        self.__targetId = targetId
        self.__ttl = ttl
        self.__traces = []
        self.__isHandled = False
    
    @public    
    def getSourceId(self):
        return self.__sourceId
    
    @public
    def getTargetId(self):
        return self.__targetId
    
    @public
    def getTTL(self):
        return self.__ttl
    
    @public
    def registerTrace(self, id):
        self.__traces.append(id)
    
    @public
    def unregisterTrace(self):
        raise NotImplementedError()
    
    @public
    def countTraces(self):
        raise NotImplementedError()
    
    @public
    def getTrace(self, index):
        raise NotImplementedError()
    
    @public
    def getTraces(self):
        raise NotImplementedError()
    
    @public
    def getFirstTrace(self):
        raise NotImplementedError()
    
    @public
    def getLastTrace(self):
        raise NotImplementedError()
    
    @public
    def getName(self):
        return self.__name
    
    @public
    def handled(self):
        self.__isHandled = True
        return self.__isHandled
    
    @public
    def isHandled(self):
        return self.__isHandled