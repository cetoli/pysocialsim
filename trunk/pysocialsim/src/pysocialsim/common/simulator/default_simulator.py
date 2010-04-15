"""
Defines the module with the implementation of DefaultSimulator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.event_dispatcher import EventDispatcher
from threading import Thread, Semaphore
from pysocialsim.common.util.rotines import requires, returns
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.common.simulator.scheduler import Scheduler

class DefaultSimulator(Object, ISimulator):
    """
    Defines the default implementation of ISimulation class.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 26/08/2009
    """

    def initialize(self):
        self.__simulation = None
        self.__eventDispatcher = EventDispatcher(self)
        self.__eventHandlingThreads = {}
        self.__scheduler = Scheduler(self)
    
    @public    
    def getSimulation(self):
        return self.__simulation

    @public
    def setSimulation(self, simulation):
        requires(simulation, ISimulation)
        self.__simulation = simulation
        self.__simulation.setSimulator(self)
        return returns(self.__simulation, ISimulation)
    
    @public    
    def handleSimulationEvent(self, simulationEvent):
        requires(simulationEvent, ISimulationEvent)
        event = returns(self.__eventDispatcher.handleSimulationEvent(simulationEvent), ISimulationEvent)
        print simulationEvent.getHandle(), simulationEvent.getPeerId()
        return event

    @public
    def registerSimulationEventHandler(self, simulationEventHandler):
        requires(simulationEventHandler, ISimulationEventHandler)
        return returns(self.__eventDispatcher.registerSimulationEventHandler(simulationEventHandler), bool)

    @public
    def unregisterSimulationEventHandler(self, handle):
        requires(handle, str)
        return returns(self.__eventDispatcher.unregisterSimulationEventHandler(handle), bool)

    @public
    def countSimulationEventHandlers(self):
        return returns(self.__eventDispatcher.countSimulationEventHandlers(), int)

    @public
    def getSimulationEventHandlers(self):
        return returns(self.__eventDispatcher.getSimulationEventHandlers(), list)

    @public
    def start(self):
        self.__simulation.configure()
        self.__simulation.execute()
        handlers = self.__eventDispatcher.getSimulationEventHandlers()
        for handler in handlers:
            eventHandlingThread = self.EventHandlingThread(self, handler.getHandle())
            self.__eventHandlingThreads[handler.getHandle()] = eventHandlingThread
            eventHandlingThread.start()
            
    @public
    def notifyEventHandlingThreads(self):
        for thread in self.__eventHandlingThreads.values():
            thread.setCurrentSimulationTime(self.__simulation.getCurrentSimulationTime())
    
    @public
    def startEventHandlingThread(self, handle):
        if self.__eventHandlingThreads.has_key(handle):
            pass
    
    @public
    def stop(self):
        self.__simulation.stop()
    
    @public    
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
            requires(simulator, ISimulator)
            requires(handle, str)
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
                        #self.simulator.handleSimulationEvent(simulation.unregisterSimulationEvent(self.__handle))
                        
                        thread = self.pool.pop(0)
                        thread.__init__(self)
                        thread.event = simulation.unregisterSimulationEvent(self.__handle)
                        thread.start()
            
        
        class ThreadForProcessing(Thread):
            
            def __init__(self, threadHandling):
                Thread.__init__(self)
                self.event = None
                self.__threadHandling = threadHandling
                
            def run(self):
                self.__threadHandling.simulator.handleSimulationEvent(self.event)
                self.__threadHandling.pool.append(self)
            
            
    simulation = property(getSimulation, setSimulation, None, None)