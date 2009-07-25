from pysocialsim.base.object import Object
from pysocialsim.simulator.dispatcher.default_dispatcher import DefaultDispatcher
from pysocialsim.base.decorator.public import public
from threading import Thread
from sets import ImmutableSet
from pysocialsim.simulator.simulation.stochastic.default_stocastich_simulation import DefaultStochasticSimulation

class DefaultSimulator(Object):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.__dispatcher = DefaultDispatcher()
    
    @public
    def handleEvent(self, event):
        return self.__dispatcher.handleEvent(event)
    
    @public
    def registerEventHandler(self, eventHandler):
        return self.__dispatcher.registerEventHandler(eventHandler)
    
    @public
    def unregisterEventHandler(self, handle):
        return self.__dispatcher.unregisterEventHandler(handle)
    
    @public
    def countEventHandlers(self):
        return self.__dispatcher.countEventHandlers()
    
    @public
    def createStochasticSimulation(self, network):
        return DefaultStochasticSimulation(self, network)
        
    @public
    def createDeterministicSimulation(self, network):
        raise NotImplementedError()
    
    @public
    def start(self, simulation):
        handlers = self.__dispatcher.getEventHandlers()
        for h in handlers:
            DefaultSimulator.EventHandlingThread(self, simulation, h.getHandle()).start()
    
    @public
    def stop(self):
        exit(0)
        
    @public
    def getEventHandlers(self):
        return ImmutableSet(self.__dispatcher.getEventHandlers())
        
    class EventHandlingThread(Thread):
        
        def __init__(self, simulator, simulation, handle):
            Thread.__init__(self)
            self.__simulator = simulator
            self.__simulation = simulation
            self.__handle = handle
        
        def run(self):
            while self.__simulation.getSimulationCurrentTime() < self.__simulation.getSimulationTime():
                while self.__simulation.countEvents(self.__handle) > 0:
                    event = self.__simulation.unregisterEvent(self.__handle)
                    self.__simulator.handleEvent(event)
