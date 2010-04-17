"""
Defines the module with the implementation of EventDispatcher class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from threading import Semaphore

class EventDispatcher(object):
    """
    Implements concrete class to dispatch simulation event for simulation event handlers.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self, simulator):
        """
        Creates an event dispatcher object.
        @param simulator: an ISimulator
        @type simulator: ISimulator
        @rtype: NoneType
        """
        self.initialize(simulator)
    
    def initialize(self, simulator):
        """
        Initializes an event dispatcher object.
        @param simulator: an ISimulator
        @type simulator: ISimulator
        @rtype: NoneType
        """
        self.__eventHandlers = {}
        self.__simulator = simulator
        self.__threads = {}
    
    
    def getSimulator(self):
        """
        Gets a simulator.
        @rtype: ISimulator
        """
        return self.__simulator

        
    def handleSimulationEvent(self, simulationEvent):
        """
        Dispatches a simulation event.
        @param simulationEvent: simulation event to be handled
        @type simulationEvent: ISimulationEvent
        @return: ISimulationEvent object
        @rtype: ISimulationEvent
        """
        if not self.__eventHandlers.has_key(simulationEvent.getHandle()):
            return None
        
        sem = Semaphore()
        sem.acquire()
        
        handler = self.__eventHandlers[simulationEvent.getHandle()]
        handlerClone = handler.clone()
        handlerClone.init(self.getSimulator().getSimulation())
        handlerClone.handleSimulationEvent(simulationEvent)
        
        sem.release()
        
        return simulationEvent
    
    
    def registerSimulationEventHandler(self, simulationEventHandler):
        """
        Registries an ISimulationEventHandler in event dispatcher.
        @param simulationEventHandler: a ISimulationEventHandler
        @type simulationEventHandler: ISimulationEventHandler
        @return: If simulation event handler already exists, it returns True. Else, it returns False
        @rtype: bool
        """
        if self.__eventHandlers.has_key(simulationEventHandler.getHandle()):
            return False
        self.__eventHandlers[simulationEventHandler.getHandle()] = simulationEventHandler
        return True
    
    
    def unregisterSimulationEventHandler(self, handle):
        """
        Unregistries a ISimulationEventHandler registerd bu event dispatcher.
        @param handle: handle of simulation event handler
        @type handle: str
        @return: If simulation event handler was removed, it returns True. Else, it returns False.
        @rtype: bool
        """
        
        if not self.__eventHandlers.has_key(handle):
            return False
        del self.__eventHandlers[handle]
        return not self.__eventHandlers.has_key(handle)
        
    
    def getSimulationEventHandlers(self):
        """
        Gets simulation event handlers registered by event dispatcher.
        @return: a list of ISimulationEventHandler objects
        @rtype: list
        """ 
        return self.__eventHandlers.values()
    
    
    def countSimulationEventHandlers(self):
        """
        Counts simulation event handlers registered by event dispatcher.
        @return: the amount of simulation event handlers
        @rtype: int
        """
        return len(self.__eventHandlers)
    
    
    
#    class EventHandlingThread(Thread):
#        """
#        Inner class to make parallel the handling of simulation events.
#        @author: Fabricio
#        @organization: Federal University of Rio de Janeiro
#        @contact: fbarros@gmail.com 
#        @since: 23/08/2009
#        """
#        
#        def __init__(self, eventDispatcher, simulationEventHandler, simulationEvent):
#            """
#            Thread constructor.
#            @param eventDispatcher: an EventDispatcher
#            @type eventDispatcher: EventDispatcher 
#            @param simulationEventHandler: an ISimulationEventHandler
#            @type simulationEventHandler: ISimulationEventHandler
#            @param simulationEvent: an ISimulationEvent
#            @type simulationEvent: ISimulationEvent
#            """
#            Thread.__init__(self)
#            requires(simulationEventHandler, ISimulationEventHandler)
#            requires(simulationEvent, ISimulationEvent)
#            
#            simulator = eventDispatcher.getSimulator()
#            
#            self.__simulationEventHandler = simulationEventHandler.clone()
#            self.__simulationEventHandler.init(simulator.getSimulation())
#            self.__simulationEvent = simulationEvent
#            logging.basicConfig(format='%(asctime)s %(event)s %(message)s', filename='myapp.log', filemode='w')
#        
#        def run(self):
#            self.__simulationEventHandler.handleSimulationEvent(self.__simulationEvent)
#            self.__simulationEvent.handled()
#            #logging.warning(str(self.__simulationEvent.getPeerId())+" "+str(self.__simulationEvent.getPriority()), extra={"event" : self.__simulationEvent.getHandle()})
#            line = self.__simulationEvent.getPriority(), self.__simulationEvent.getHandle(), self.__simulationEvent.getPeerId()
#            
#            self.__dispatcherLogFile = open("simulation.log", "a")
#            self.__dispatcherLogFile.write(str(line)+"\n")
#            self.__dispatcherLogFile.close()
            