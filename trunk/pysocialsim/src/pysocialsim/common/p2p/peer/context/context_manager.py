from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public

class ContextManager(Object):
    
    def __init__(self, peer):
        self.initialize(peer)
            
    def initialize(self, peer):
        self.__peer = peer
        self.__contexts = {}
    
    @public    
    def getPeer(self):
        return self.__peer
    
    @public
    def registerContext(self, type, context):
        aux = False
        if not self.__contexts.has_key(type):
            self.__contexts[type] = {}
        
        contextByType = self.__contexts[type]
        
        if not contextByType.has_key(context.getId()):
            contextByType[context.getId()] = context
            aux = True
            
        return aux
    
    @public
    def updateContext(self, type, context):
        if not self.__contexts.has_key(type):
            return False
        
        contextByType = self.__contexts[type]
        if not contextByType.has_key(context.getId()):
            return False
        
        contextByType[context.getId()] = context
        return True
        
    
    @public
    def getContexts(self, type):
        aux = [].__iter__()
        if self.__contexts.has_key(type):
            aux = self.__contexts[type].itervalues()
        return aux
    
    @public
    def hasContext(self, type, contextId):
        if not self.__contexts.has_key(type):
            return False
        
        return self.__contexts[type].has_key(contextId)
    
    @public
    def getContext(self, type, contextId):
        if not self.__contexts.has_key(type):
            return None
        
        contextByType = self.__contexts[type]
        
        if not contextByType.has_key(contextId):
            return None
        
        return contextByType[contextId]