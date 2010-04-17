"""
Defines the module with the implementation of DefaultSimulator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/08/2009
"""
from pysocialsim.simulator.i_simulator import ISimulator
from pysocialsim.simulator.event.event_dispatcher import EventDispatcher
from pysocialsim.simulator.scheduler import Scheduler
from threading import Thread

class DefaultSimulator(ISimulator):
    """
    Defines the default implementation of ISimulation class.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 26/08/2009
    """

    def __init__(self):
        self.initialize()

    def initialize(self):
        self.__simulation = None
        self.__eventDispatcher = EventDispatcher(self)
        self.__eventHandlingThreads = {}
        self.__scheduler = Scheduler(self)
    
        
    def getSimulation(self):
        return self.__simulation

    
    def setSimulation(self, simulation):
        self.__simulation = simulation
        self.__simulation.setSimulator(self)
        return self.__simulation
    
        
    def handleSimulationEvent(self, simulationEvent):
        event = self.__eventDispatcher.handleSimulationEvent(simulationEvent)
        print simulationEvent.getHandle(), simulationEvent.getPeerId()
        return event

    
    def registerSimulationEventHandler(self, simulationEventHandler):
        return self.__eventDispatcher.registerSimulationEventHandler(simulationEventHandler)

    
    def unregisterSimulationEventHandler(self, handle):
        return self.__eventDispatcher.unregisterSimulationEventHandler(handle)

    
    def countSimulationEventHandlers(self):
        return self.__eventDispatcher.countSimulationEventHandlers()

    
    def getSimulationEventHandlers(self):
        return self.__eventDispatcher.getSimulationEventHandlers()

    
    def start(self):
        self.__simulation.configure()
        self.__simulation.execute()
        handlers = self.__eventDispatcher.getSimulationEventHandlers()
        for handler in handlers:
            eventHandlingThread = self.EventHandlingThread(self, handler.getHandle())
            self.__eventHandlingThreads[handler.getHandle()] = eventHandlingThread
            eventHandlingThread.start()
            
    
    def notifyEventHandlingThreads(self):
        for thread in self.__eventHandlingThreads.values():
            thread.setCurrentSimulationTime(self.__simulation.getCurrentSimulationTime())
    
    
    def startEventHandlingThread(self, handle):
        if self.__eventHandlingThreads.has_key(handle):
            pass
    
    
    def stop(self):
        self.__simulation.stop()
    
        
    def getScheduler(self):
        return self.__scheduler
    
    class EventHandlingThread(Thread):
        """
        Thread for headling events.
        @author: Fabricio
        @organization: Federal University of Rio de Janeiro
        @contact: fbarros@gmail.com 
        @since: 26/08/2009
        """
        
        def __init__(self, simulator, handle):
            """
            Creates a thread event handling thread.
            @param simulator: an ISimulator
            @type simulator: ISimulator
            @param handle: a str
            @type handle: str
            @rtype: NoneType
            """
            Thread.__init__(self)
            self.simulator = simulator
            self.__handle = handle
            self.__currentSimulationTime = 0
            self.pool = []
            for i in range(5):
                self.pool.append(self.ThreadForProcessing(self))
            
        def setCurrentSimulationTime(self, currentSimulationTime):
            self.__currentSimulationTime = currentSimulationTime
        
        def run(self):
            simulation = self.simulator.getSimulation()
            while True:
                event = simulation.getSimulationEvent(self.__handle)
                if event and len(self.pool) > 0:
                    if self.__currentSimulationTime >= event.getPriority():
                        if self.__currentSimulationTime >= 7000:
                            self.simulator.handleSimulationEvent(simulation.unregisterSimulationEvent(self.__handle))
                        else:
                            thread = self.pool.pop(0)
                            thread.__init__(self)
                            thread.event = simulation.unregisterSimulationEvent(self.__handle)
                            try:
                                thread.start()
                            except:
                                continue
            
        
        class ThreadForProcessing(Thread):
            
            def __init__(self, threadHandling):
                Thread.__init__(self)
                self.event = None
                self.__threadHandling = threadHandling
                
            def run(self):
                self.__threadHandling.simulator.handleSimulationEvent(self.event)
                self.__threadHandling.pool.append(self)
            
            
    simulation = property(getSimulation, setSimulation, None, None)