"""
Defines the module with the specification of ISimulator interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""

class ISimulator(object):
    """
    Define the interface of simulator objects.
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
        @param simulationEvent: an ISimulationEvent
        @type simulationEvent: ISimulationEvent
        @return: an ISimulationEvent object.
        @rtype: ISimulationEvent
        """
        raise NotImplementedError()
    
    def registerSimulationEventHandler(self, simulationEventHandler):
        """
        Registries an ISimulationEventHandler object.
        @param simulationEventHandler: an ISimulationEventHandler
        @type simulationEventHandler: ISimulationEventHandler
        @return: If simulation event handler already exists, it returns True. Else, it returns False
        @rtype: bool
        """
        raise NotImplementedError()
    
    def unregisterSimulationEventHandler(self, handle):
        """
        Unregistries a ISimulationEventHandler registerd bu event dispatcher.
        @param handle: handle of simulation event handler
        @type handle: str
        @return: If simulation event handler was removed, it returns True. Else, it returns False.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def countSimulationEventHandlers(self):
        """
        Counts simulation event handlers registered by event dispatcher.
        @return: the amount of simulation event handlers
        @rtype: int
        """
        raise NotImplementedError()
    
    def getSimulationEventHandlers(self):
        """
        Gets simulation event handlers registered by event dispatcher.
        @return: a list of ISimulationEventHandler objects
        @rtype: list
        """
        raise NotImplementedError()
    
    def start(self):
        """
        Starts the simulator.
        @rtype: NoneType
        """
        raise NotImplementedError()
    
    def stop(self):
        """
        Stops the simulator
        @rtype: NoneType
        """
        raise NotImplementedError()
    
    def setSimulation(self, simulation):
        """
        Configures the simulator with a simulation.
        @param simulation: an ISimulation
        @type simulation: ISimulation
        @return: an ISimulation object
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def getSimulation(self):
        """
        Gets a simulation object.
        @return: an ISimulation object
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def getScheduler(self):
        """
        Gets the scheduler of simulator.
        @return: a Scheduler
        @rtype: Scheduler
        """
        raise NotImplementedError()
    
    def notifyEventHandlingThreads(self):
        raise NotImplementedError()
    
    def startEventHandlingThread(self, handle):
        raise NotImplementedError()
    
    