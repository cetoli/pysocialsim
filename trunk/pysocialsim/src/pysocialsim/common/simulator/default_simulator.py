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
from threading import Thread
from pysocialsim.common.util.rotines import requires, returns
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent
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
        return returns(self.__eventDispatcher.handleSimulationEvent(simulationEvent), ISimulationEvent)

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
            self.__simulator = simulator
            self.__handle = handle
        
        def run(self):
            simulation = self.__simulator.getSimulation()
            while simulation.countSimulationEvents(self.__handle) > 0:
                event = simulation.getSimulationEvent(self.__handle)
                if simulation.getCurrentSimulationTime() == event.getPriority():
                    self.__simulator.handleSimulationEvent(simulation.unregisterSimulationEvent(self.__handle))
        
    class ExitSimulationEvent(AbstractSimulationEvent):
        
        def __init__(self):
            self.__handle = "EXIT"
        
        @public
        def getHandle(self):
            return self.__handle

    simulation = property(getSimulation, setSimulation, None, None)