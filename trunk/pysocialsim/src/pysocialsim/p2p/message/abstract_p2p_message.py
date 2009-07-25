from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from sets import ImmutableSet

class AbstractP2PMessage(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, name, id,  sourceId, targetId, ttl, priority):
        self.__id = id
        self.__name = name
        self.__sourceId = sourceId
        self.__targetId = targetId
        self.__ttl = ttl
        self.__traces = []
        self.__isHandled = False
        self.__hop = 0
        self.__priority = priority
        self.__parameters = {}
    
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
        if isinstance(id, bool):
            raise TypeError()
        self.__traces.append(id)
        return id
    
    @public
    @return_type(int)
    def unregisterTrace(self):
        if len(self.__traces) == 0:
            raise StandardError()
        return self.__traces.pop(len(self.__traces) - 1)
        
    
    @public
    @return_type(int)
    def countTraces(self):
        return len(self.__traces)
    
    @public
    @return_type(int)
    @require("index", int)
    def getTrace(self, index):
        return self.__traces[index]
    
    @public
    @return_type(list)
    def getTraces(self):
        return self.__traces
    
    @public
    @return_type(int)
    def getFirstTrace(self):
        if len(self.__traces) == 0:
            raise StandardError()
        return self.__traces[0]
    
    @public
    @return_type(int)
    def getLastTrace(self):
        if len(self.__traces) == 0:
            raise StandardError()
        
        return self.__traces[len(self.__traces) - 1]
    
    @public
    @return_type(str)
    def getName(self):
        return self.__name
    
    @public
    @return_type(bool)
    def handled(self):
        self.__isHandled = True
        return self.__isHandled
    
    @public
    @return_type(bool)
    def isHandled(self):
        return self.__isHandled
    
    @public
    @return_type(int)
    @require("hop", int)
    def setHop(self, hop):
        self.__hop = hop
        return self.__hop
        
    @public
    @return_type(int)
    def getHop(self):
        return self.__hop
    
    @public
    @return_type(int)
    @require("sourceId", int)
    def setSourceId(self, sourceId):
        self.__sourceId = sourceId
    
    @public
    @return_type(int)
    @require("targetId", int)
    def setTargetId(self, targetId):
        self.__targetId = targetId
        
    @public    
    def clone(self):
        raise NotImplementedError()
    
    @public
    @return_type(object)
    @require("name", str)
    @require("value", object)
    def setParameter(self, name, value):
        self.__parameters[name] = value
        return self.__parameters[name]
        
    @public
    @return_type(object)
    @require("name", str)
    def getParameter(self, name):
        return self.__parameters[name]
    
    @public
    @return_type(object)
    @require("name", str)
    def removeParameter(self, name):
        value = self.__parameters[name]
        del self.__parameters[name]
        return value
        
    @public
    @return_type(int)
    def getId(self):
        return self.__id
    
    @public
    @return_type(int)
    def countParameters(self):
        return len(self.__parameters)
    
    @public
    @return_type(int)
    def getPriority(self):
        return self.__priority
    
    @public
    def getParameterNames(self):
        return ImmutableSet(self.__parameters.keys())
    
    @public
    def getParameterValues(self):
        return ImmutableSet(self.__parameters.values())