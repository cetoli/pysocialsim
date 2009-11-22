"""
Defines the module with the implement AbstractContext class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 05/11/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.base.decorators import public

class AbstractContext(Object, IContext):
    

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, type, id, peer):
        self.__type = type
        self.__id = id
        self.__tags = []
        self.__peer = peer
    
    @public
    def getPeer(self):
        return self.__peer
        
    @public
    def getType(self):
        return self.__type

    @public
    def getId(self):
        return self.__id

    @public
    def getTags(self):
        return self.__tags.__iter__()
    
    @public
    def registerTag(self, tag):
        if tag in self.__tags:
            return False
        self.__tags.append(tag)
        return tag in self.__tags
    
    @public
    def unregisterTag(self, tag):
        if not tag in self.__tags:
            return False
        self.__tags.remove(tag)
        return not tag in self.__tags
    
    @public
    def countTags(self):
        return len(self.__tags)
    

    type = property(getType, None, None, None)

    id = property(getId, None, None, None)

    tags = property(getTags, None, None, None)

    peer = property(getPeer, None, None, None)
        
    