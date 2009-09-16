"""
Defines the module with objective the implementation of AbstractPeer class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.base.decorators import public

class AbstractPeer(Object, IPeer):
    """
    Defines the abstract implementation of IPeer interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, type, id):
        """
        Initializes the object.
        @param type: the type of peer
        @type type: int
        @param id: the identifier of peer.
        @type id: int
        """
        self.__id = id
        self.__type = type
    
    @public    
    def getId(self):
        return self.__id
    
    @public
    def getType(self):
        return self.__type

    id = property(getId, None, None, None)

    type = property(getType, None, None, None)
        
    
        