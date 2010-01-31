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

    def initialize(self, type, id):
        self.__type = type
        self.__id = id
        self.__version = 1
        
    @public
    def getVersion(self):
        return self.__version

    @public
    def setVersion(self, version):
        self.__version = version
        
    @public
    def getType(self):
        return self.__type

    @public
    def getId(self):
        return self.__id

    type = property(getType, None, None, None)

    id = property(getId, None, None, None)    
    
    version = property(getVersion, setVersion, None, None)
