'''
Created on 02/02/2010

@author: fabricio
'''
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.content.i_content import IContent
from pysocialsim.common.base.decorators import public

class Content(Object, IContent):
    
    def __init__(self, id, size):
        self.initialize(id, size)
    
    def initialize(self, id, size):
        self.__id = id
        self.__size = size
        self.__contents = []
        
    @public
    def getId(self):
        return self.__id
    
    @public
    def getSize(self):
        return self.__size
    
    @public
    def registerOwner(self, peerId):
        if peerId in self.__contents:
            return False
        
        self.__contents.append(peerId)
        return peerId in self.__contents
    
    @public
    def unregisterOwner(self, peerId):
        if not peerId in self.__contents:
            return False
        
        self.__contents.remove(peerId)
        return not peerId in self.__contents
    
    @public
    def countOwners(self):
        return len(self.__contents)
    
    @public
    def getOwners(self):
        return self.__contents