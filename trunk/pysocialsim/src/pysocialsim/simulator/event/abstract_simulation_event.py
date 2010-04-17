"""
Defines the module with the implementation of AbstractSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.simulator.event.i_simulation_event import ISimulationEvent

class AbstractSimulationEvent(ISimulationEvent):
    """
    Abstract class that implemenents the ISimulationEvent interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    
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
        self.__handle = handle
        self.__peerId = peerId
        self.__priority = priority
        self.__isHanlded = False
        self.__parameters = {}
    
    
    def getHandle(self):
        return self.__handle

    
    def getPeerId(self):
        return self.__peerId
    
    
    def setPeerId(self, peerId):
        self.__peerId = peerId
        return self.__peerId

    
    def getPriority(self):
        return self.__priority
    
    
    def handled(self):
        self.__isHanlded = True

    
    def isHandled(self):
        return self.__isHanlded
    
    
    def registerParameter(self, name, value):
        self.__parameters[name] = value
        
    
    def hasParameter(self, name):
        return self.__parameters.has_key(name)
    
    
    def getParameter(self, name):
        try:
            value = self.__parameters[name]
        except:
            raise KeyError("Nao entendi: " + self.__parameters.__str__())
             
        return value
    
    def __eq__(self, other):
        if not other:
            return False
        return self.__handle == other.getHandle() and self.__peerId == other.getPeerId() and self.__priority == other.getPriority()