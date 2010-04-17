"""
Defines the module with the specification of ISimulationEventHandler.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 24/08/2009
"""

class ISimulationEventHandler(object):
    """
    Defines the interface of simulation event handler objects.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def handleSimulationEvent(self, simulationEvent):
        """
        Handles a simulation event.
        @param simulationEvent: a ISumulationEvent object
        @type simulationEvent: ISimulationEvent
        @return: a ISimulationEvent
        @rtype: ISimulationEvent 
        """
        raise NotImplementedError()
    
    def getHandle(self):
        """
        Gets the handle of simulation event handler.
        @return: a str object.
        @rtype: str
        """
        raise NotImplementedError()
    
    def clone(self):
        """
        Creates a new object from prototype instance.
        @return: an ISimulationEventHandler
        @rtype: ISimulationEventHandler
        """
        raise NotImplementedError()
    
    def getSimulationEvent(self):
        """
        Gets a simulation event.
        @return: an ISimulationEvent
        @rtype: ISimulationEvent
        """
        raise NotImplementedError()
    
    def getSimulation(self):
        """
        Gets a simulation.
        @return: a ISimulation
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def init(self, simulation):
        """
        Initialize a prototype instance.
        @param simulation: a ISimulation
        @type simulation: ISimulation
        @rtype: NoneType
        """
        raise NotImplementedError()