'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.sharing.i_sharing import ISharing
from pysocialsim.common.base.decorators import public

class AbstractSharing(Object, ISharing):
    
    def __init__(self):
        raise NotImplementedError()

    def initialize(self, id, peer, sharingType):
        self.__id = id
        self.__peer = peer
        self.__sharingType = sharingType
    
    @public
    def getId(self):
        return self.__id

    @public
    def getPeer(self):
        return self.__peer

    @public
    def getSharingType(self):
        return self.__sharingType

    
    