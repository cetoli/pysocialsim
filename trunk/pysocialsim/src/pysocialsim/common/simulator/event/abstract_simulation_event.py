"""
Defines the module with the implementation of AbstractSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, returns

class AbstractSimulationEvent(ISimulationEvent, Object):
    """
    Abstract class that implemenents the ISimulationEvent interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    @public
    def initialize(self, handle, peerId, priority):
        """
        Initializes the object.
        @param handle: handle of simulation event
        @type handle: str
        @param peerId: peerId of simulation event
        @type peerId: int
        @param priority: priority of simulation event.
        @type priority: int
        @rtype: None
        @note: All simulation events are initialized as unhandled.
        """
        requires(handle, str)
        requires(peerId, int)
        requires(priority, int)
        
        self.__handle = handle
        self.__peerId = peerId
        self.__priority = priority
        self.__isHanlded = False
    
    @public
    def getHandle(self):
        return returns(self.__handle, str)

    @public
    def getPeerId(self):
        return returns(self.__peerId, int)

    @public
    def getPriority(self):
        return returns(self.__priority, int)
    
    @public
    def handled(self):
        self.__isHanlded = True

    @public
    def isHandled(self):
        return self.__isHanlded
    
    def __eq__(self, other):
        if not other:
            return False
        return self.__handle == other.getHandle() and self.__peerId == other.getPeerId() and self.__priority == other.getPriority()
    
    handle = property(getHandle, None, None, None)
    """
    @type: str 
    """

    peer = property(getPeerId, None, None, None)
    """
    @type: IPeer 
    """

    priority = property(getPriority, None, None, None)
    """
    @type: int 
    """
    
    